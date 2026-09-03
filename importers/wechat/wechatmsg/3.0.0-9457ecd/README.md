# WeChatMsg 3.0.0 历史源码

- 固定原作者提交：[`9457ecdad74826ebede9a040b1d86d986c968f1e`](https://github.com/LC044/WeChatMsg/commit/9457ecdad74826ebede9a040b1d86d986c968f1e)。这不是仍可领取的 GitHub 安装包 tag。
- 原样源码：[WeChatMsg-9457ecdad74826ebede9a040b1d86d986c968f1e.tar.gz](WeChatMsg-9457ecdad74826ebede9a040b1d86d986c968f1e.tar.gz)。
- Git tree：`f0ff70068c3ab2ba1592afbb2f684b821d9d0209`；264 个文件。
- 根许可：[原始 MIT LICENSE](LICENSE.upstream)，Copyright 2024 SiYuan。上游打包的 FFmpeg 等组件仍有各自的权利和许可边界。
- 恢复线索：[tqjason/WeChatMsg](https://github.com/tqjason/WeChatMsg/tree/14b466dcc4c60b43d9d79301e489c8d6029daed4) 的 merge 包含该原作者提交，应用代码未改，仅增加同步工作流。

上游明确声明此提交适配 Windows 微信 4.0.3；3.x 支持来自离散版本配置，4.1.x 未经本项目验证。上游不支持 Win7 / macOS；没有可靠证据将本站归档标为 Windows 所有版本可运行。

源码内已有 `example/3-exporter.py` 和 `example/README.md`，无需本项目重写导出器。但示例需要用户配置输入、联系人和依赖，不是完整命令行产品；依赖清单还存在未列出 `python-docx` 等限制。本项目未安装或运行它，也不执行数据获取、解密或账号密钥相关示例。

选用此工具时，保留 HTML、配套 `.html.json` 和所选媒体；不要把 `exporter/exporter_json.py` 的训练数据输出当作原始聊天备份。详见[聊天导出说明](../../../../docs/CHAT_IMPORT.md)与[工具目录](../../../README.md)。
