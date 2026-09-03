# 分层许可

仓库中的不同材料采用不同许可，不能用一个总许可覆盖所有来源。

| 范围 | 默认许可 |
|---|---|
| `src/`、`tests/`、CLI、Schema、workflow、Agent skills 与本项目编写的 `importers/verify_archives.py` | Apache License 2.0；标准正文见根目录 `LICENSE` |
| 贡献者原创的 Markdown 叙事 | Creative Commons Attribution-ShareAlike 4.0 International |
| 贡献者原创的结构化元数据与派生索引 | CC0 1.0 Universal |
| 第三方网页、文件、照片、录音、视频与引文 | 以对应 `source` 记录为准；未明示即不授予额外权利 |
| `importers/wechat/` 中的第三方源码归档及上游许可证副本 | 保持各固定提交的原许可与声明，见 [工具目录](importers/README.md) 与各版本文件夹；不适用本项目 Apache-2.0/CC0 默认许可 |

对应标准文本：

- Apache-2.0：<https://www.apache.org/licenses/LICENSE-2.0>
- CC BY-SA 4.0：<https://creativecommons.org/licenses/by-sa/4.0/legalcode>
- CC0 1.0：<https://creativecommons.org/publicdomain/zero/1.0/legalcode>

提交原创内容即表示有权按上述对应许可提供该部分。链接、哈希或来源元数据不意味着项目取得第三方原件的版权。

CipherTalk 桌面源码声明 CC BY-NC-SA 4.0 并附上游说明，不能因其 `CipherTalk-CLI` 子目录为 MIT 就把桌面版改标为 MIT。本次 WeChatMsg 固定源码的根许可证为 MIT；其归档中包含的第三方组件仍需按各自声明判断，不能由根许可证推导所有原生二进制均已完成许可审查。本项目未修改这两份源码归档；保留原始作者信息、许可及文件树用于追溯。工具使用许可不授予公开他人聊天内容的权利。
