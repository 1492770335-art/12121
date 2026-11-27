> 2026-11-27 本地文件导入更新：7份PDF已转换；A01/B01全文补齐；当前222条入口，79条有公开全文，135条仅本地，8条未取得。公开原始PDF75份，XML7份，Markdown/TXT各82份。此前正文统计为历史快照。详见[本轮记录](local_imports/desktop_20261127/README.md)及[最新统一索引](index.csv)。

# 全文库构建与许可核查报告

日期：2026-11-27T01:13:48.843191+08:00。研究检索截止仍为2026-11-26。

本轮核查上一批208个有全文的paper_id条目及其补充/版本文件，并继续获取13篇核心文献。已建立类别/paper_id目录，不修改既有论文、假设、估计方法或模拟实验。

## 实际成果

- 上一批208个paper_id全部纳入逐文件许可审计，共213条paper_id/哈希记录。发现两组跨ID的同哈希文件，见duplicate_files.json；因此208不等于208份不同PDF。
- 共221个入口目录；79个条目有公开全文、132个条目仅本地可读、10篇核心正文仍未取得。
- 公开原始文件按SHA去重：74份PDF、7份JATS XML；配套81份Markdown、81份TXT。
- 保留121个原始.tex文件，来自27个arXiv版本源包；4个已许可arXiv版本源入口未取得TeX，见latex_acquisition.csv。
- 本地受限PDF另外生成136条逐页Markdown/TXT转换记录，全部位于local_private/，未上传全文。
- 221份原创版本/定位/精读准备札记；1966个公开PDF页面标有数学核对提示。未声称已逐式人工复核。

## 数学与分页

所有原始PDF/XML与作者TeX均按字节保留，校验SHA256。PDF Markdown/TXT按物理页分段，page_map.json同时给出GitHub读取需要的行号范围；印刷页码候选与PDF标签单独记录。定理、引理、假设、证明等实际观察标签及页码/行号见theorem_proof_locator.csv。公式未被猜测性重写或修正。

仅有XML的条目没有伪造PDF分页。JATS的原始TeX-math和MathML保留在转换稿及original_formula_markup.json中。原始PDF文件仍在获取失败的XML条目，保留失败来源与原因，不能把XML称为PDF。

## 未公开原因

arXiv默认非独占分发许可未授予第三方再分发权；作者主页或机构存档公开可读也不自动授予上传权。下列为逐文件记录的原因分布，不能作为独立论文数量相加：

```json
{
  "arxiv_nonexclusive_no_further_reuse_grant": 97,
  "arxiv_license_requires_review": 1,
  "license_not_confirmed": 38
}
```

原始材料保持各自CC BY / BY-NC / BY-NC-ND / BY-NC-SA等条件；本库为非商业学术研究用途。ND文件仅作技术格式转换，原始文件完整保留，不翻译或改写。权利及转换规则见CONVERSION_AND_RIGHTS.md。

## 13篇核心文献的本轮状态

|paper_id|正文|补充新取得|公开PDF|
|---|---|---:|---:|
|A01|not_acquired|0|0|
|B01|not_acquired|0|0|
|C01|local_only|0|0|
|D01|not_acquired|0|0|
|D02|not_acquired|0|0|
|D04|not_acquired|0|0|
|D05|not_acquired|0|0|
|G01|not_acquired|0|0|
|G02|local_only|0|0|
|G04|not_acquired|0|0|
|G08|local_only|1|0|
|I03|not_acquired|0|0|
|K01|not_acquired|0|0|

新取得正文为C01收益—风险约束规则、G02 Cox、G08竞争风险随机森林；G08另取得独立补充。均尚未确认可公开再分发，保存本地。其余10篇仍未取得，具体HTTP/非PDF失败、原文路径见core_acquisition_attempts.csv和core_status.csv。没有绕过付费墙、CAPTCHA、登录或TDM token要求。

## 复核与局限

完整性校验见validation.json。其检查原始文件哈希、页数及逐页分段、作者TeX字节、索引路径和许可白名单。原PDF页面经抽样渲染检查；未对全部数学公式作视觉逐式审校。OCR未被用来补写没有文本层的页；读者须回原页或作者TeX核对。

这些阅读札记是依据实际资料建立的精读准备和定位记录，不是已经完成的理论评述。原始TeX的外部样式、图片和数据没有被自动公开；源码未编译，不能承诺独立编译成功。
