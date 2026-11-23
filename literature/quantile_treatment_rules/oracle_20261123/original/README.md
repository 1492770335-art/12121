# 原始 Oracle 结果包的无损归档

该目录保存用户 2026-11-23 上传的 **`Oracle_竞争风险决策_20261123_结果包.zip`**，原始二进制字节不变，分为 8 个 GitHub Blob。按顺序拼接 `.part` 文件即可完全恢复原 ZIP。

| 分片 | 原始字节数 | Git Blob SHA-1 |
|---|---:|---|
| 01 | 524288 | `48991ff569c235b5ceec3283de26f0a6bc8d9ea9` |
| 02 | 524288 | `2f4d559e66547b2ad8d05226665af3b34fad1a64` |
| 03 | 524288 | `41d5dd0638a4b12812175dbf56438a077b404892` |
| 04 | 524288 | `4b4bf81e1d8185efd513198520577755a43ba910` |
| 05 | 524288 | `f8c3bd0cb8456f3f5c0c729fa3cf1f030a0bc5b8` |
| 06 | 524288 | `7a1aceb66705180e5c85805173e8ce3bf5c69b18` |
| 07 | 524288 | `58f85247b9f666b2c757875a911f22f3cca183e5` |
| 08 | 205268 | `d3b397dcea0da07e24ade929908b154cc82cfdae` |

完整原 ZIP 长度 **3,875,284** 字节，SHA-256：

`4700ea52b9a50c0d96786965ad4fe13e30b0b40952292bc396700699c34a06b7`

在仓库该目录下运行：

```bash
python restore.py
```

或者使用二进制拼接（类 Unix shell）：

```bash
cat oracle-result.part01 oracle-result.part02 oracle-result.part03 oracle-result.part04 oracle-result.part05 oracle-result.part06 oracle-result.part07 oracle-result.part08 > Oracle_竞争风险决策_20261123_结果包.zip
sha256sum Oracle_竞争风险决策_20261123_结果包.zip
```

还原脚本会检查各分片大小、总长度与完整文件 SHA-256。ZIP 自带原始中文报告、配置、40 余项源码/结果/图像/测试文件，避免通过复制粘贴造成 CSV 或图片失真。原始归档中的风险机制、数值表和原生报告**未被修改**。