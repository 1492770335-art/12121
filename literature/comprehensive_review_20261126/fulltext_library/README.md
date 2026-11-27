> 2026-11-27 本地文件导入更新：7份PDF已转换；A01/B01全文补齐；当前222条入口，79条有公开全文，135条仅本地，8条未取得。公开原始PDF75份，XML7份，Markdown/TXT各82份。此前正文统计为历史快照。详见[本轮记录](local_imports/desktop_20261127/README.md)及[最新统一索引](index.csv)。

# 可公开全文与精读入口

本目录用于通过GitHub按paper_id读取资料。文件的许可、版本和数学保真度均单独记录。全文仅公开在明确许可允许的范围内；NC/ND/SA条件继续适用。本库用于非商业学术研究，不授予超出原许可的使用权。

PDF保持原始字节不变。Markdown/TXT按原始PDF物理页分段，不重构或纠正公式；每个含数学符号或公式编号的页面均提示核对原PDF。作者原始TeX以字节及SHA256保留，未编译。XML来源没有可验证PDF分页时，使用结构化章节索引，并明确写明无PDF分页。

## 统计

```json
{
  "entries": 221,
  "baseline_paper_ids": 208,
  "baseline_artifact_records": 213,
  "all_audited_artifact_records": 219,
  "unique_audited_hashes": 216,
  "public_entries": 79,
  "local_only_entries": 132,
  "not_acquired_entries": 10,
  "public_unique_artifacts": 81,
  "public_original_pdf": 74,
  "public_original_xml": 7,
  "public_markdown": 81,
  "public_txt": 81,
  "original_tex_files": 121,
  "reading_notes": 221,
  "formula_flagged_pages": 1966,
  "core_new_fulltexts": 3,
  "built_at": "2026-11-27T01:10:09.453058+08:00"
}
```

## 读取方法

先读[index.csv](index.csv)或[index.json](index.json)，再按条目的public_markdown/public_txt/original_tex路径读取。大文件可用GitHub fetch_file的start_line/end_line分段。公式页标记见[formula_page_flags.json](formula_page_flags.json)。原文、转换稿、原始TeX和补充材料不能互相替代。

完整许可逐文件记录见[license_audit.csv](license_audit.csv)、[new_artifact_audit.csv](new_artifact_audit.csv)以及各artifact下provenance_and_license.json。hash重复记录见[duplicate_files.json](duplicate_files.json)。

## 文献入口

|paper_id|类别|状态|原始PDF|Markdown|TeX文件数|
|---|---|---|---|---|---:|
|[A01](A/A01/README.md)|A|not_acquired|0|0|0|
|[A02](A/A02/README.md)|A|public_fulltext|1|1|45|
|[A03](A/A03/README.md)|A|local_only|0|0|0|
|[A04](A/A04/README.md)|A|local_only|0|0|0|
|[A08](A/A08/README.md)|A|public_fulltext|1|1|0|
|[A12](A/A12/README.md)|A|local_only|0|0|0|
|[B01](B/B01/README.md)|B|not_acquired|0|0|0|
|[B02](B/B02/README.md)|B|local_only|0|0|0|
|[B03](B/B03/README.md)|B|local_only|0|0|0|
|[B05](B/B05/README.md)|B|local_only|0|0|0|
|[B06](B/B06/README.md)|B|local_only|0|0|0|
|[B08](B/B08/README.md)|B|local_only|0|0|0|
|[B10](B/B10/README.md)|B|local_only|0|0|0|
|[C01](C/C01/README.md)|C|local_only|0|0|0|
|[C02](C/C02/README.md)|C|public_fulltext|1|1|0|
|[C03](C/C03/README.md)|C|local_only|0|0|0|
|[C09](C/C09/README.md)|C|local_only|0|0|0|
|[D01](D/D01/README.md)|D|not_acquired|0|0|0|
|[D02](D/D02/README.md)|D|not_acquired|0|0|0|
|[D03](D/D03/README.md)|D|local_only|0|0|0|
|[D04](D/D04/README.md)|D|not_acquired|0|0|0|
|[D05](D/D05/README.md)|D|not_acquired|0|0|0|
|[D16](D/D16/README.md)|D|local_only|0|0|0|
|[D19](D/D19/README.md)|D|local_only|0|0|0|
|[E01](E/E01/README.md)|E|local_only|0|0|0|
|[E02](E/E02/README.md)|E|local_only|0|0|0|
|[E03](E/E03/README.md)|E|local_only|0|0|0|
|[E09](E/E09/README.md)|E|local_only|0|0|0|
|[E10](E/E10/README.md)|E|local_only|0|0|0|
|[E14](E/E14/README.md)|E|local_only|0|0|0|
|[G01](G/G01/README.md)|G|not_acquired|0|0|0|
|[G02](G/G02/README.md)|G|local_only|0|0|0|
|[G04](G/G04/README.md)|G|not_acquired|0|0|0|
|[G08](G/G08/README.md)|G|local_only|0|0|0|
|[G09](G/G09/README.md)|G|local_only|0|0|0|
|[G18](G/G18/README.md)|G|local_only|0|0|0|
|[H01](H/H01/README.md)|H|local_only|0|0|0|
|[H02](H/H02/README.md)|H|local_only|0|0|0|
|[H03](H/H03/README.md)|H|local_only|0|0|0|
|[H04](H/H04/README.md)|H|local_only|0|0|0|
|[H05](H/H05/README.md)|H|local_only|0|0|0|
|[H06](H/H06/README.md)|H|local_only|0|0|0|
|[H07](H/H07/README.md)|H|local_only|0|0|0|
|[H13](H/H13/README.md)|H|public_fulltext|1|1|0|
|[I01](I/I01/README.md)|I|local_only|0|0|0|
|[I03](I/I03/README.md)|I|not_acquired|0|0|0|
|[I05](I/I05/README.md)|I|local_only|0|0|0|
|[I06](I/I06/README.md)|I|local_only|0|0|0|
|[I07](I/I07/README.md)|I|local_only|0|0|0|
|[I10](I/I10/README.md)|I|public_fulltext|0|1|0|
|[I12](I/I12/README.md)|I|public_fulltext|0|1|0|
|[I14](I/I14/README.md)|I|public_fulltext|1|2|3|
|[J01](J/J01/README.md)|J|local_only|0|0|0|
|[J05](J/J05/README.md)|J|local_only|0|0|0|
|[J08](J/J08/README.md)|J|local_only|0|0|0|
|[K01](K/K01/README.md)|K|not_acquired|0|0|0|
|[N00475a7280](I/N00475a7280/README.md)|I|public_fulltext|1|1|0|
|[N01917c91ad](E/N01917c91ad/README.md)|E|local_only|0|0|0|
|[N028b5c1a3a](G/N028b5c1a3a/README.md)|G|public_fulltext|1|1|0|
|[N046da13c5e](E/N046da13c5e/README.md)|E|public_fulltext|1|1|1|
|[N051ce5894a](E/N051ce5894a/README.md)|E|local_only|0|0|0|
|[N0823fd9721](D/N0823fd9721/README.md)|D|public_fulltext|1|1|0|
|[N09cb4bece0](A/N09cb4bece0/README.md)|A|local_only|0|0|0|
|[N0ac9e6598e](C/N0ac9e6598e/README.md)|C|public_fulltext|1|1|1|
|[N0bfdddd54f](K/N0bfdddd54f/README.md)|K|public_fulltext|1|1|0|
|[N0ce1953394](E/N0ce1953394/README.md)|E|local_only|0|0|0|
|[N0d9d6017c6](B/N0d9d6017c6/README.md)|B|local_only|0|0|0|
|[N0e05636762](E/N0e05636762/README.md)|E|local_only|0|0|0|
|[N1378943fc0](E/N1378943fc0/README.md)|E|local_only|0|0|0|
|[N14a6119231](I/N14a6119231/README.md)|I|local_only|0|0|0|
|[N15d33bad80](B/N15d33bad80/README.md)|B|local_only|0|0|0|
|[N194983acec](I/N194983acec/README.md)|I|public_fulltext|1|1|0|
|[N1ac4f08798](E/N1ac4f08798/README.md)|E|local_only|0|0|0|
|[N1e85cdf87a](I/N1e85cdf87a/README.md)|I|public_fulltext|1|1|0|
|[N1eab6bd9fd](C/N1eab6bd9fd/README.md)|C|local_only|0|0|0|
|[N20f409afc5](I/N20f409afc5/README.md)|I|local_only|0|0|0|
|[N24139fb199](H/N24139fb199/README.md)|H|local_only|0|0|0|
|[N276158539f](H/N276158539f/README.md)|H|local_only|0|0|0|
|[N2765752d40](E/N2765752d40/README.md)|E|local_only|0|0|0|
|[N288e5a522a](D/N288e5a522a/README.md)|D|local_only|0|0|0|
|[N2941ef20c4](I/N2941ef20c4/README.md)|I|public_fulltext|1|1|0|
|[N2a302256fd](D/N2a302256fd/README.md)|D|local_only|0|0|0|
|[N2a95c580ee](I/N2a95c580ee/README.md)|I|public_fulltext|1|1|0|
|[N2b4fb3717a](B/N2b4fb3717a/README.md)|B|public_fulltext|0|1|0|
|[N2c37bd1c6b](G/N2c37bd1c6b/README.md)|G|local_only|0|0|0|
|[N3281d86b6b](A/N3281d86b6b/README.md)|A|local_only|0|0|0|
|[N32b0137644](E/N32b0137644/README.md)|E|public_fulltext|1|1|12|
|[N3452219253](I/N3452219253/README.md)|I|local_only|0|0|0|
|[N36296d1e95](H/N36296d1e95/README.md)|H|public_fulltext|1|1|0|
|[N3824d9fed2](G/N3824d9fed2/README.md)|G|local_only|0|0|0|
|[N3828b7b80c](A/N3828b7b80c/README.md)|A|local_only|0|0|0|
|[N396530134e](A/N396530134e/README.md)|A|local_only|0|0|0|
|[N39eca4fc6b](K/N39eca4fc6b/README.md)|K|public_fulltext|1|2|0|
|[N3d4c1276f4](E/N3d4c1276f4/README.md)|E|local_only|0|0|0|
|[N3f53d9b17e](B/N3f53d9b17e/README.md)|B|public_fulltext|1|1|0|
|[N3ff37abd04](G/N3ff37abd04/README.md)|G|public_fulltext|1|1|0|
|[N405fee7bdb](D/N405fee7bdb/README.md)|D|local_only|0|0|0|
|[N407705ee75](A/N407705ee75/README.md)|A|local_only|0|0|0|
|[N476cce5c63](A/N476cce5c63/README.md)|A|public_fulltext|1|1|18|
|[N47e3cac5c2](K/N47e3cac5c2/README.md)|K|public_fulltext|1|1|0|
|[N47fbb24f26](E/N47fbb24f26/README.md)|E|public_fulltext|1|1|1|
|[N49bddfe389](G/N49bddfe389/README.md)|G|local_only|0|0|0|
|[N4a06cb65c7](B/N4a06cb65c7/README.md)|B|local_only|0|0|0|
|[N4a323d5212](K/N4a323d5212/README.md)|K|public_fulltext|1|1|0|
|[N4b1a5277af](E/N4b1a5277af/README.md)|E|local_only|0|0|0|
|[N4e7406b8e8](K/N4e7406b8e8/README.md)|K|public_fulltext|1|1|0|
|[N5012c76a1e](A/N5012c76a1e/README.md)|A|local_only|0|0|0|
|[N5330e2a82e](E/N5330e2a82e/README.md)|E|public_fulltext|1|1|1|
|[N5533d0166c](E/N5533d0166c/README.md)|E|public_fulltext|1|1|1|
|[N57f4f38eaa](E/N57f4f38eaa/README.md)|E|local_only|0|0|0|
|[N5a18097227](B/N5a18097227/README.md)|B|public_fulltext|1|1|1|
|[N5ab4794283](D/N5ab4794283/README.md)|D|local_only|0|0|0|
|[N5fd3d78779](B/N5fd3d78779/README.md)|B|public_fulltext|1|1|0|
|[N62cce2101f](G/N62cce2101f/README.md)|G|local_only|0|0|0|
|[N644d9bd31a](A/N644d9bd31a/README.md)|A|local_only|0|0|0|
|[N64f9dce05a](G/N64f9dce05a/README.md)|G|local_only|0|0|0|
|[N65ca0da421](B/N65ca0da421/README.md)|B|public_fulltext|1|1|5|
|[N67821c653f](A/N67821c653f/README.md)|A|public_fulltext|1|1|45|
|[N6820de5fe0](K/N6820de5fe0/README.md)|K|public_fulltext|1|1|0|
|[N6a5930c2a3](E/N6a5930c2a3/README.md)|E|local_only|0|0|0|
|[N6c42d911f8](G/N6c42d911f8/README.md)|G|public_fulltext|1|1|0|
|[N6dd6af3b8b](B/N6dd6af3b8b/README.md)|B|local_only|0|0|0|
|[N707653ca70](A/N707653ca70/README.md)|A|local_only|0|0|0|
|[N744317b6fa](D/N744317b6fa/README.md)|D|local_only|0|0|0|
|[N75a31268f1](H/N75a31268f1/README.md)|H|local_only|0|0|0|
|[N7626df45b1](D/N7626df45b1/README.md)|D|local_only|0|0|0|
|[N76921dc5a5](E/N76921dc5a5/README.md)|E|local_only|0|0|0|
|[N7896ad9ac8](E/N7896ad9ac8/README.md)|E|public_fulltext|1|1|0|
|[N79365aacdf](A/N79365aacdf/README.md)|A|public_fulltext|1|1|2|
|[N79781aca35](E/N79781aca35/README.md)|E|local_only|0|0|0|
|[N7a6c477885](K/N7a6c477885/README.md)|K|public_fulltext|1|1|0|
|[N7a78cb7524](D/N7a78cb7524/README.md)|D|local_only|0|0|0|
|[N7be47e5be1](E/N7be47e5be1/README.md)|E|local_only|0|0|0|
|[N7de102edb2](K/N7de102edb2/README.md)|K|local_only|0|0|0|
|[N7f33210eb1](A/N7f33210eb1/README.md)|A|public_fulltext|1|1|2|
|[N7fd9155413](K/N7fd9155413/README.md)|K|public_fulltext|1|1|0|
|[N80c05fe96e](K/N80c05fe96e/README.md)|K|public_fulltext|1|1|0|
|[N80e1501cd8](A/N80e1501cd8/README.md)|A|local_only|0|0|0|
|[N811db572b0](B/N811db572b0/README.md)|B|local_only|0|0|0|
|[N838715a6ca](B/N838715a6ca/README.md)|B|local_only|0|0|0|
|[N84dc638faf](G/N84dc638faf/README.md)|G|local_only|0|0|0|
|[N8850eb0883](E/N8850eb0883/README.md)|E|local_only|0|0|0|
|[N8e49951c41](E/N8e49951c41/README.md)|E|public_fulltext|1|1|0|
|[N8e87d06011](C/N8e87d06011/README.md)|C|local_only|0|0|0|
|[N9033f59cd7](K/N9033f59cd7/README.md)|K|local_only|0|0|0|
|[N93d7eb2e44](E/N93d7eb2e44/README.md)|E|public_fulltext|1|1|1|
|[N95905e1815](G/N95905e1815/README.md)|G|local_only|0|0|0|
|[N96664c0d36](A/N96664c0d36/README.md)|A|public_fulltext|1|1|1|
|[N982a041314](K/N982a041314/README.md)|K|public_fulltext|0|1|0|
|[N9929e90163](D/N9929e90163/README.md)|D|local_only|0|0|0|
|[N9b1dd316c7](I/N9b1dd316c7/README.md)|I|public_fulltext|1|1|0|
|[N9b80218d73](E/N9b80218d73/README.md)|E|local_only|0|0|0|
|[N9e1c1189b2](D/N9e1c1189b2/README.md)|D|local_only|0|0|0|
|[N9f2d975ad9](B/N9f2d975ad9/README.md)|B|public_fulltext|1|1|0|
|[Na40930f34f](C/Na40930f34f/README.md)|C|local_only|0|0|0|
|[Na5caa5dea2](K/Na5caa5dea2/README.md)|K|local_only|0|0|0|
|[Na6d152153e](A/Na6d152153e/README.md)|A|local_only|0|0|0|
|[Na799c3a418](I/Na799c3a418/README.md)|I|local_only|0|0|0|
|[Na994f1a30c](E/Na994f1a30c/README.md)|E|local_only|0|0|0|
|[Naad07d29b4](E/Naad07d29b4/README.md)|E|local_only|0|0|0|
|[Nab85168a63](K/Nab85168a63/README.md)|K|public_fulltext|1|1|0|
|[Nabaf548cd2](I/Nabaf548cd2/README.md)|I|public_fulltext|1|2|0|
|[Nabc60b4d4b](C/Nabc60b4d4b/README.md)|C|local_only|0|0|0|
|[Nad7defd0a4](D/Nad7defd0a4/README.md)|D|local_only|0|0|0|
|[Naee6721bcd](K/Naee6721bcd/README.md)|K|public_fulltext|1|1|0|
|[Nb00c3293c8](K/Nb00c3293c8/README.md)|K|local_only|0|0|0|
|[Nb0df1d2cda](E/Nb0df1d2cda/README.md)|E|local_only|0|0|0|
|[Nb38cc254e4](E/Nb38cc254e4/README.md)|E|local_only|0|0|0|
|[Nba074a7ea6](E/Nba074a7ea6/README.md)|E|local_only|0|0|0|
|[Nbb8696d04c](E/Nbb8696d04c/README.md)|E|local_only|0|0|0|
|[Nbbecc5ccd4](D/Nbbecc5ccd4/README.md)|D|public_fulltext|1|1|0|
|[Nbd8e9b1943](K/Nbd8e9b1943/README.md)|K|local_only|0|0|0|
|[Nbdce5360b5](G/Nbdce5360b5/README.md)|G|public_fulltext|1|1|3|
|[Nbdd6947c84](H/Nbdd6947c84/README.md)|H|public_fulltext|1|1|1|
|[Nbdf1d0399c](E/Nbdf1d0399c/README.md)|E|public_fulltext|1|1|0|
|[Nbe184fd2d7](K/Nbe184fd2d7/README.md)|K|local_only|0|0|0|
|[Nc000c7871f](C/Nc000c7871f/README.md)|C|public_fulltext|1|1|0|
|[Nc335d00d40](G/Nc335d00d40/README.md)|G|local_only|0|0|0|
|[Nc372dd64c2](E/Nc372dd64c2/README.md)|E|public_fulltext|1|1|1|
|[Nc3de79e114](G/Nc3de79e114/README.md)|G|public_fulltext|1|1|0|
|[Nc5a05d2563](E/Nc5a05d2563/README.md)|E|local_only|0|0|0|
|[Nc5b13297f5](B/Nc5b13297f5/README.md)|B|local_only|0|0|0|
|[Nc6b55d6c2b](G/Nc6b55d6c2b/README.md)|G|public_fulltext|1|1|0|
|[Nc94f4ec76e](E/Nc94f4ec76e/README.md)|E|local_only|0|0|0|
|[Nc9cc8b8a6a](G/Nc9cc8b8a6a/README.md)|G|local_only|0|0|0|
|[Ncb07b047d0](E/Ncb07b047d0/README.md)|E|public_fulltext|1|1|0|
|[Ncb290ba0be](D/Ncb290ba0be/README.md)|D|public_fulltext|1|1|4|
|[Ncb5c244489](K/Ncb5c244489/README.md)|K|public_fulltext|1|1|0|
|[Nccc0e9b69b](E/Nccc0e9b69b/README.md)|E|local_only|0|0|0|
|[Ncec770af7b](H/Ncec770af7b/README.md)|H|public_fulltext|1|1|10|
|[Ncf6983f2c0](E/Ncf6983f2c0/README.md)|E|local_only|0|0|0|
|[Ncf8cccde6d](K/Ncf8cccde6d/README.md)|K|public_fulltext|1|1|0|
|[Ncfd3d4fb59](H/Ncfd3d4fb59/README.md)|H|local_only|0|0|0|
|[Nd01dfe732f](D/Nd01dfe732f/README.md)|D|local_only|0|0|0|
|[Nd22b7f030f](B/Nd22b7f030f/README.md)|B|public_fulltext|1|1|1|
|[Nd30f15a7cd](D/Nd30f15a7cd/README.md)|D|local_only|0|0|0|
|[Nd793378d58](A/Nd793378d58/README.md)|A|public_fulltext|1|1|0|
|[Nd9c954e0a6](K/Nd9c954e0a6/README.md)|K|local_only|0|0|0|
|[Ndb0a17dd4e](G/Ndb0a17dd4e/README.md)|G|public_fulltext|1|1|1|
|[Ndc14ca11a5](E/Ndc14ca11a5/README.md)|E|local_only|0|0|0|
|[Ndc8c37146e](A/Ndc8c37146e/README.md)|A|public_fulltext|1|1|1|
|[Ndf5ed6286f](A/Ndf5ed6286f/README.md)|A|local_only|0|0|0|
|[Ndfdff87fd0](K/Ndfdff87fd0/README.md)|K|public_fulltext|1|1|0|
|[Ne0c8b93065](B/Ne0c8b93065/README.md)|B|local_only|0|0|0|
|[Ne4d9c36f04](E/Ne4d9c36f04/README.md)|E|public_fulltext|1|1|1|
|[Ne4f398fbfc](E/Ne4f398fbfc/README.md)|E|local_only|0|0|0|
|[Ne84f1c3263](K/Ne84f1c3263/README.md)|K|public_fulltext|1|1|0|
|[Ne9bc8fe99e](E/Ne9bc8fe99e/README.md)|E|local_only|0|0|0|
|[Nea68e38ddb](B/Nea68e38ddb/README.md)|B|public_fulltext|1|1|1|
|[Neee3693a21](I/Neee3693a21/README.md)|I|public_fulltext|1|1|0|
|[Nf0e3866bb7](E/Nf0e3866bb7/README.md)|E|local_only|0|0|0|
|[Nf265d6eaff](A/Nf265d6eaff/README.md)|A|local_only|0|0|0|
|[Nf2c4076178](B/Nf2c4076178/README.md)|B|public_fulltext|1|1|1|
|[Nf5ce55e86a](I/Nf5ce55e86a/README.md)|I|public_fulltext|1|1|0|
|[Nf5d5055cf4](C/Nf5d5055cf4/README.md)|C|public_fulltext|1|1|1|
|[Nf7a912c6e6](K/Nf7a912c6e6/README.md)|K|public_fulltext|1|1|0|
|[Nf7f81a38bb](K/Nf7f81a38bb/README.md)|K|local_only|0|0|0|
|[Nfa85d8db32](I/Nfa85d8db32/README.md)|I|public_fulltext|1|1|0|
|[Nfcadcb0fdc](H/Nfcadcb0fdc/README.md)|H|public_fulltext|1|1|0|
|[Nfcd9532f69](B/Nfcd9532f69/README.md)|B|local_only|0|0|0|
|[Nfe45b0a8ff](E/Nfe45b0a8ff/README.md)|E|local_only|0|0|0|
