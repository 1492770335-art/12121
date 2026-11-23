"""Independent checks on archived source, targeted replay, and saved tables."""
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from analyze_existing_oracle import HERE, METRICS, SCENARIOS, calibrate, replay_one, source_from_archive


class EXP02Consistency(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp=tempfile.TemporaryDirectory(prefix="exp02_test_source_")
        cls.root,cls.oracle=source_from_archive(Path(cls.temp.name))
        cls.out=HERE/"results"

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_exact_legacy_replication(self):
        historical=pd.read_csv(self.root/"results/pairs_raw.csv")
        a=pd.read_csv(self.out/"replicate_candidate_counts.csv")
        for scenario in SCENARIOS:
            old=historical[(historical.scenario==scenario)&(historical.method=="RMET-Q1")&
                           (historical.subset=="changed")].sort_values("rep")
            new=a[(a.scenario==scenario)&(a.category=="legacy_action_mismatch")].sort_values("rep")
            np.testing.assert_array_equal(new["count"],old["count"])
            self.assertEqual(len(old),200)
            self.assertEqual(int(new["count"].sum()),25106 if scenario=="PH_tradeoff" else 20974)

    def test_replay_and_protection_invariants(self):
        calibration=pd.read_csv(self.out/"calibration_audit.csv").set_index("scenario")
        for scenario in SCENARIOS:
            ci=self.oracle.SCENARIOS.index(scenario)
            budget,match=calibrate(self.oracle,scenario,ci)
            self.assertAlmostEqual(12*budget,calibration.loc[scenario,"delta_R_month"])
            self.assertAlmostEqual(100*match,calibration.loc[scenario,"matched_both_candidates_pct"])
            a,b,c,patients,_=replay_one(self.oracle,scenario,ci,1,budget)
            self.assertEqual(next(x["count"] for x in a if x["category"]=="Q1_tie"),0)
            self.assertEqual(next(x["count"] for x in a if x["category"]=="legacy_vs_unified_Q"),0)
            self.assertEqual(next(x["count"] for x in a if x["category"]=="legacy_vs_unified_R"),0)
            self.assertTrue(all(x["strict_interior"]==1 for x in patients))
            all_row=next(x for x in b if x["subset"]=="all")
            # These cross-budget violations are allowed: the two rules
            # guarantee their own, not each other's, protection constraint.
            self.assertLessEqual(all_row["q_budget_violation_sum"],all_row["count"])
            self.assertLessEqual(all_row["r_budget_violation_sum"],all_row["count"])

    def test_population_decomposition_and_reachability(self):
        b=pd.read_csv(self.out/"replicate_outcome_sums.csv")
        c=pd.read_csv(self.out/"replicate_heterogeneity_sums.csv")
        for scenario in SCENARIOS:
            for rep in range(1,201):
                x=b[(b.scenario==scenario)&(b.rep==rep)].set_index("subset")
                self.assertEqual(int(x.loc["all","count"]),5000)
                self.assertEqual(int(x.loc["strict_interior","count"]),5000)
                self.assertEqual(int(x.loc["changed","count"]),int(x.loc["changed_strict_interior","count"]))
                for col in [j+"_sum" for j in METRICS]:
                    self.assertAlmostEqual(x.loc["all",col],x.loc["changed",col],places=9)
                y=c[(c.scenario==scenario)&(c.rep==rep)].set_index("group")
                self.assertEqual(int(y.loc["near_cap_boundary","count"]),0)
                self.assertEqual(int(y.loc["priority_unreachable_any","count"]),0)
                self.assertEqual(int(y.loc["all_unreachable_any","count"]),0)
                self.assertEqual(int(y.loc[[f"Z1_Q{q}_Z2_{z}" for q in range(1,5) for z in (0,1)],"count"].sum()),5000)

    def test_saved_patient_and_candidate_counts(self):
        a=pd.read_csv(self.out/"table_A_candidate_sets.csv")
        patients=pd.read_csv(self.out/"changed_patients.csv")
        for scenario in SCENARIOS:
            counts=a[a.scenario==scenario].set_index("category")["count"]
            changed=patients[patients.scenario==scenario]
            self.assertEqual(len(changed),counts["action_mismatch"])
            self.assertLessEqual(counts["action_mismatch"],counts["candidate_mismatch"])
            self.assertEqual(counts["Q1_tie"],0)
            self.assertTrue((changed.d_Q!=changed.d_R).all())
            self.assertTrue((changed.strict_interior==1).all())
            self.assertTrue((changed.A_Q_0+changed.A_Q_1>=1).all())
            self.assertTrue((changed.A_R_0+changed.A_R_1>=1).all())


if __name__=="__main__":
    unittest.main(verbosity=2)
