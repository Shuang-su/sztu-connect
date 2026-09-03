# 完成记录

日期：2026-09-03。项目：SZTU Connect。

## 交付结果

本地实现和校验已完成；提交、main 集成与远端读回结果将在本记录的交付检查点补齐。

- 根目录新增 [工具目录](../../../importers/README.md) 和 [登记表](../../../importers/registry.json)，保存 CipherTalk-SafeFork 与 WeChatMsg 两份固定源码快照、许可副本与来源说明。
- CipherTalk `v2026.829.0` 的 DMG / EXE 使用上游固定 Release 直链；本轮没有下载、安装、重托管或执行安装包，没有配置 Git LFS。
- 更新 `map-chat-to-events`、`record-campus-event`、`fact-check-event` 和 [聊天工作流](../../CHAT_IMPORT.md)，让原始导出可直接作为 Source，不把 JSONL 转换设为必要门槛。
- 完成 [比较研究报告](../../research/2026-09-03-chat-export-tools.md)，其他四条路线仅登记固定来源和支持边界；无新微信解析器、公开 CLI/API 或平台 Schema。
- README 只调整相关入口、目录与致谢/许可描述；没有改写已有首页文案、其他任务的记录规则或隐私扫描实现。

## 来源与实际文件验证

| 项目 | 实际源码字节数 | 文件数 | 实际 SHA-256 |
|---|---:|---:|---|
| CipherTalk-SafeFork `acf221c11ecb1afae32e88885b2309dd39f0f161` | 39412192 | 927 | `fb4dd7f75320dd3b301d8c62f8f76731b03ff08a35b4f3e1da7c1e5fb365dffa` |
| WeChatMsg `9457ecdad74826ebede9a040b1d86d986c968f1e` | 58035722 | 264 | `ceb16f1ef59ad3fec58fba41b6001a717ca79a9c0e5a0b660fae33626ae633bd` |

两份源码来自 GitHub 官方 codeload 的完整提交地址，未重新打包。逐文件重算 Git blob/tree，与 GitHub 固定提交 API 的 tree 完全一致：CipherTalk 为 `6096cdfa8aa85439f6a377a9313ba3b25aecc365`，WeChatMsg 为 `f0ff70068c3ab2ba1592afbb2f684b821d9d0209`。独立许可副本均与归档内原件相同，包括 WeChatMsg 原许可证没有结尾换行这一字节细节。

安装包摘要仅从上游 Release API 读取并明确标注；两条实际下载入口 HEAD 均为 HTTP 200。报告、工具目录和聊天说明中的 43 个去重外部链接均完成 HEAD 可达性检查；链接可达不替代正文证据或二进制验收。

## 测试与检查

- `python3 importers/verify_archives.py`：两份源码的 SHA-256、大小、文件树、路径与许可检查通过，不联网、不解包、不运行上游代码。
- 全量单元测试：**67 项通过**，其中新增 **14 项** 存档回归测试，覆盖损坏、内容替换、许可替换、固定提交、路径冲突、越界、链接、特殊成员、容量限制、Git 签出字节保真和失败输出。
- 三个修改技能均通过 skill-creator 的 `quick_validate.py`；Python 编译检查通过。
- `doctor`、`validate --json`、`privacy-scan --json`、`check --json` 通过。正式 Event / Node / Collection / Source 均保持 0，不把第三方工具或虚构测试导入正式索引。
- 隐私扫描为 `block: 0, review: 6`：两份 tar.gz 和三个非标准扩展名的许可副本被标为未扫描二进制；另一个手机号模式命中实际是公开 GitHub Actions run ID。许可文本与归档文本已另行读取检查，不通过修改扫描器压掉提示。
- 两次构建的 **12 个派生文件逐个 SHA-256 相同**，`data/generated/` 无 Git 差异。
- 仓库的虚构 JSONL 示例校验通过，本地通用 HTML 渲染成功；不是平台导出器运行测试。
- Markdown 内链、围栏与研究报告副本一致性检查覆盖此次 13 份文档、61 处本地链接；视觉渲染未作验收，不将结构检查称为完整视觉审核。
- 本项目编写文件的 `git diff --check` 通过；CipherTalk 上游许可原文有 4 处既存行尾空格，按字节保真要求保留，没有为消除样式提示改写许可证。该原文例外不影响源码树或许可副本的完整性检查。

## 技能场景检查与修正

使用独立测试者和两条明确虚构的消息，测试选工具、JSONL 映射与来源独立性；没有提供真实账号或聊天数据，也没有运行第三方软件。

首轮发现现有 CLI 的 `ingest --dry-run` 仍会写出 `.work/intake/…/manifest.json`，与测试“只写指定输出目录”的约束冲突。已修正两个相关技能和共享文档：严格只读或不允许 `.work/` 写入时仅做只读文件/哈希检查；需要并获准保留清单时才运行 ingest；同样说明 renderer 的 `.work/` 输出限制。没有改动 CLI 行为。

首轮额外产生的 818 字节虚构输入清单已移入私有测试输出目录保留，没有删除用户原件。输入文件前后 SHA-256 均为 `a3d48f2eb049946c512bbefd6653c9dc0de700b64407b03f623bf0d1ebda5625`。修正后复测只在指定目录生成 JSONL 与映射说明，两条 19 位消息 ID 保持字符串、回复可解析、原始时间表达留存，JSONL 校验通过；没有再次生成 intake 清单或写正式记录。

其他两个场景也得到正确的有限答复：Intel Mac + 桌面微信 4.1 没有匹配的现有安装包；同一群聊的重导出与截图不能直接计为三个独立来源。测试者没有为初核问题虚构 Event、消息位置、日期或已检查原件的状态。另据观察补充 fact-check-event 的“尚无 Event 时先做有限初核”入口，并重新进行结构校验。

## 研究过程与局限

Deep research 使用指定四个项目及两个实质不同的替代路线，先检查原作者提交、发行版、许可与 forks，再定向核对微信版本、打包产物、来源链和消息字段；以原始文件和元数据支持结论。内部保留报告源、claim/source ledger、证据缺口矩阵和查询/停止依据；公开报告包含核心证据、限制和停止理由。

通用网页工具曾不可用，关键事实改用直接 GitHub API、固定源文件、构建日志和 Gitee 公开 refs 验证。开发环境首次跳过构建隔离安装时缺少 setuptools 后端；按项目声明恢复标准隔离安装后成功，未修改依赖锁或全局环境。

文本凭据模式检查实际读取 CipherTalk 769 个、WeChatMsg 113 个可解码文本文件。命中项为代码表达式、配置键、占位内容或模型数据的小数数字片段；本次未识别出真实凭据。其余二进制及图片内容没有完成恶意软件、可复现构建或全组件许可审计，不能据此保证软件安全。

已知边界：

- 不保证所有现行微信小版本；没有 Windows/macOS 安装包运行和真实聊天导出验收。
- CipherTalk 构建日志显示跳过签名；保存者名称、SHA-256 或 Git tree 不能证明作者身份、无恶意行为或聊天未事先编辑。
- CipherTalk 桌面非商业/相同方式共享许可、CLI 的 MIT，以及 WeChatMsg 自身与内含依赖的许可分别保留，不重新许可。
- 基线 README、PRIVACY 和 content override 存在与新技能“私有原件和公开授权分别判断”不一致的既有表述。本次未擅自改动这些无关规则；这仍是后续使用真实材料前需要解决的集成风险。本次只有公开软件和虚构测试，无真实材料发布。
- Source 的来源定位与聊天内容是否真实是两回事，工具文件和许可不授予公开他人聊天的权利。

## Git 检查点与远端交付

- 起点：`main` / `origin/main` = `eb30c774db2f76752a0ed6d9da02ee42d6aeac11`，原 checkout 干净。
- 隔离分支：`codex/chat-tool-archives`；缓存、下载暂存、报告源、测试输入与测试输出均留在忽略的项目工作目录。
- 本地检查点、远端 SHA 与 CI 结果：交付时补充，不预先宣称已推送。
- 已确认交付目标为 main；不创建 PR、Release、tag 或部署，不强推，不改写用户已有历史。
