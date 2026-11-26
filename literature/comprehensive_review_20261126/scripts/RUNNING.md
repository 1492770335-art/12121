# 运行与复核

Python 3.13。实际依赖版本见 dependency_versions.json。运行目录为仓库根目录。

```powershell
python -m pip install pypdf fonttools pymupdf cryptography bibtexparser
python literature/comprehensive_review_20261126/scripts/collect.py
python literature/comprehensive_review_20261126/scripts/enrich.py
python literature/comprehensive_review_20261126/scripts/resolve_remaining.py
python literature/comprehensive_review_20261126/scripts/extra_sources.py
python literature/comprehensive_review_20261126/scripts/core_followup.py
python literature/comprehensive_review_20261126/scripts/local_materials.py
python literature/comprehensive_review_20261126/scripts/acquire.py --priority P0
python literature/comprehensive_review_20261126/scripts/acquire.py --priority P1
python literature/comprehensive_review_20261126/scripts/acquire.py --priority P2
python literature/comprehensive_review_20261126/scripts/code_sources.py
python literature/comprehensive_review_20261126/scripts/expand.py
python literature/comprehensive_review_20261126/scripts/supplementary_trace.py
python literature/comprehensive_review_20261126/scripts/acquire.py --new-only --priority P1
python literature/comprehensive_review_20261126/scripts/assemble.py
python literature/comprehensive_review_20261126/scripts/validate.py
python literature/comprehensive_review_20261126/scripts/final_metrics.py
```

不要并行运行写同一状态文件的步骤。`collect.py`和`expand.py`分别保存主状态与扩展状态到`local_private/`；网络响应按URL哈希缓存。失败尝试保留在manifest，已下载文件必须经文件签名、标题、页数、字节数、SHA256核验。重跑不执行任何下载得到的脚本。

连接失败最多重试一次并退避，HTTP 400/401/403/404不重试；不绕过登录、CAPTCHA或付费墙。不使用虚构的联系邮箱或API token。没有调用Unpaywall、认证版Google Scholar、Web of Science或Scopus。HTTP缓存的早期版本没有保留重定向后的最终URL；这些记录的final_url留空，不以源URL伪装为最终URL。

`local_materials.py`读取本次环境中已有的四份PDF，路径为`D:/最后一版/参考文献原文`；这是显式的本地材料导入，移至其他机器时应调整路径或跳过。导入不会把受限本地文件上传GitHub。JMLR及DVK官方PDF的额外获取保留来源在manifest，原始缓存仅存本地。

检索规模有界：关键词每个检索取前100条；OpenAlex每个节点前向最多400条；第二层取30个相关近邻。补充追踪首次前向页最多200条。总命中数与实际取回数分别记录，未完成队列不能视为已筛查。新文献按题名初筛和Crossref/Europe PMC书目核验入库，适用性还需摘要和全文复审。

`search_log_seed_replay.csv`是基于同一URL缓存重建并复跑的种子核验日志，已标注cache-assisted audit replay。不能将缓存复核次数当作新增文献数。`publication_status.csv`保留Crossref更正关系，不宣称穷尽撤回通知。`citation_edges_supplementary.csv`的候选尚待后续书目和适用性筛选。

公开同步使用文件白名单：本目录中原创CSV/BibTeX/报告/脚本/许可证据，以及manifest明确带可再分发许可的`open_access/`文件。`local_private/`、环境变量、凭据、脚本缓存不提交。作者代码ZIP保留本地，公开记录固定commit、license、原始链接和哈希。
