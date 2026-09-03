# 聊天导出工具选型与来源存档研究

面向：SZTU Connect 的使用者与维护者

核查日期：2026-09-03

决策范围：复用现成导出工具，保存可追溯的版本与许可；不开发平台解析器，不处理真实账号或聊天数据。

## 结论

保留 **CipherTalk-SafeFork 2026.829.0 作为主要下载入口，WeChatMsg 3.0.0 的原作者固定提交作为 Windows 历史源码备用**。本次实际保存这两份完整源码快照；CipherTalk 的 DMG、EXE 只提供固定上游 Release 链接，不下载重托管，不配置 Git LFS。入口、实际源码摘要和安装包上游摘要见 [工具目录](../../importers/README.md)。

在本次核查到的版本中，没有证据支持某个桌面替代品同时在**来源链、原始字段保留、现成安装包和已验证兼容性**上全面优于这个组合。这里的“主要”是本项目在限定证据下的选择，不是安全认证或运行成功保证。

- PyWxDump、wechatDataBackup 已找到可定位的历史存档，但主要是旧 Windows 3.x 路线，不能作为现行 4.x 的默认替代。
- WeFlow 5.1.0 的平台覆盖更广，但所见备份明确自述为网络收集，缺少原作者连续历史；更丰富的功能不能补足这项来源缺口。
- WechatExporter 有原作者固定发行版，适合作为 **iPhone/iPad 本地备份**的条件性补充，不是桌面微信数据库工具。

上述判断的逐项证据在下文。所有兼容性均区分“文档或源码证据”和“真实运行验证”；本次没有运行任何第三方导出工具。

## 比较口径

“可信来源”拆成三个独立问题：

1. **工具来源**：来自哪个作者/保存者、哪一个不可含糊的提交，存档是否与该 Git 文件树相同，适用什么许可。
2. **收到的导出文件**：保留哪一份原件、接收时的 SHA-256、实际导出工具版本、会话范围、原始消息定位和已知处理过程。
3. **发言中的事情是否成立**：仍需上下文、独立来源与反证。文件摘要不能证明接收前未被编辑，工具名中有 “Safe” 也不能证明聊天真实。

工具登记表不进入校园 Source 索引。用户提供的原始导出可以直接作为聊天 Source，不强制先转 JSONL；具体字段与工作流见 [聊天导出与来源引用](../CHAT_IMPORT.md)。

## 固定版本与适用边界

| 工具及固定版本 | 适用范围的证据 | 可取得的形态 | 本次处置 |
|---|---|---|---|
| CipherTalk-SafeFork 2026.829.0，`acf221c…` | 上游说明 Windows 10/11；发布构建为 Windows x64、macOS arm64。未找到完整、精确到所有微信小版本的实测矩阵。 | 固定 Release DMG/EXE、固定源码 | 两份平台安装包使用上游链接；保存源码 |
| WeChatMsg 3.0.0，`9457ecd…` | 原作者明确提交微信 4.0.3 适配；157 个离散 3.x 配置；不支持 Win7/macOS 的上游限制仍在 | 原作者历史源码、可核对的直接 fork；未确认相同提交的持久安装包 | 保存源码，标记“历史备用”，不冒充一装即用 |
| PyWxDump 3.1.45，`d62e846…` | 固定配置有 66 个离散 3.x 版本，最高 3.9.12.55；无 4.x 条目；FAQ 指向 Windows 10 x64 或更新 | 同提交的直接 fork | 仅登记旧版本线索 |
| wechatDataBackup 1.2.4，`260c730…` | Windows 旧路线；作者在快照之后仍说明 4.0 适配进行中 | GitHub 历史提交；Gitee 同提交与标签 | 仅登记，不扩称 4.x 可用 |
| WeFlow 5.1.0，`3c58317…` | 备份 README 声称 4.0+，发行包覆盖 Windows x64/arm64、macOS arm64、Linux x64；未实测 | 网络收集型备份的源码与 Release | 仅研究，不替换主要入口 |
| WechatExporter 1.9.5.13，`474318a…` | 未加密 iOS 本地备份；历史测试包含 iOS 15.4、手机微信 8.0.18；Windows/macOS x64 发行包 | 原作者固定 Release | 仅列为 iOS 备份路线 |

表中的版本号不是连续兼容区间。配置中存在某个版本不等于本项目已验证该版本；手机微信 8.x 与桌面微信 4.x 也不是可直接比较的版本序列。完整提交和结构化元数据见 [registry.json](../../importers/registry.json)，各行的原始证据如下。

## 1. CipherTalk-SafeFork：保留来源链，但不把 SafeFork 当作认证

### 版本和发布证据

选定提交为 `acf221c11ecb1afae32e88885b2309dd39f0f161`，Git tree 为 `6096cdfa8aa85439f6a377a9313ba3b25aecc365`。该提交只修改更新服务文件，父提交 `098f15e2fa2a6b879bdf18d6741eb0229921beb9` 可由 olansoft 保存链定位；由内容历史建立联系，而不是仅根据仓库名字判断来自原作者。该提交的 GitHub 签名验证字段为 false。[mintleaf84，固定提交，2026-09-01](https://github.com/mintleaf84/CipherTalk-SafeFork/commit/acf221c11ecb1afae32e88885b2309dd39f0f161)、[olansoft，保留的父提交](https://github.com/olansoft/CipherTalk-SafeFork/commit/098f15e2fa2a6b879bdf18d6741eb0229921beb9)

`v2026.829.0` 发布于 2026-09-01，而不是由文件名推测的 8 月 29 日。GitHub API 给出 DMG 的 221,408,494 字节和 EXE 的 162,366,374 字节及其 SHA-256，且 Release 的 `immutable` 为 false。安装包摘要已登记为“上游 API 摘要”，没有标成“本地下载计算”。两条下载入口经 HEAD 检查可达，仍可能被上游删除或替换。[mintleaf84，Release 元数据](https://api.github.com/repos/mintleaf84/CipherTalk-SafeFork/releases/tags/v2026.829.0)

发布构建的 Windows 与 macOS 任务成功，分别为 x64 和 arm64；日志显示跳过签名。工作流整体失败发生在额外 R2 镜像任务，不等于两个 GitHub 安装包都未构建成功。反过来，构建成功也不能证明安全或兼容性。[mintleaf84，发布构建记录，2026-09-01](https://github.com/mintleaf84/CipherTalk-SafeFork/actions/runs/33525868161)

### 导出是否利于溯源

桌面详细 JSON 同时输出解析内容与 `rawContent`，保留字符串 `platformMessageId`、时间、发言者和回复信息；`localId` 存在数组序号回退逻辑。因而建议以详细 JSON 原件加所选媒体作为接收对象，并在引用中区分服务器 ID 与局部定位。这个选择来自固定导出代码，不是界面功能名称。[mintleaf84，exportService.ts，固定快照](https://github.com/mintleaf84/CipherTalk-SafeFork/blob/acf221c11ecb1afae32e88885b2309dd39f0f161/electron/services/exportService.ts)

桌面根许可为 CC BY-NC-SA 4.0 并附上游说明，`CipherTalk-CLI` 子项目另有 MIT 许可；不能把 CLI 的许可或精简导出契约推广到桌面安装包。本地分别保留两个许可的原始字节。[桌面许可证](https://github.com/mintleaf84/CipherTalk-SafeFork/blob/acf221c11ecb1afae32e88885b2309dd39f0f161/LICENSE)、[CLI 许可证](https://github.com/mintleaf84/CipherTalk-SafeFork/blob/acf221c11ecb1afae32e88885b2309dd39f0f161/CipherTalk-CLI/LICENSE)

**剩余限制：**此次 SafeFork 改动针对强制更新获取，不等于去除全部网络行为或原生组件授权逻辑。原生依赖的完整来源、可复现构建、安装包签名和现行微信补丁兼容性没有完成独立验证。不得以存档为由跳过系统保护或推导无需授权访问账号。[更新服务改动](https://github.com/mintleaf84/CipherTalk-SafeFork/commit/acf221c11ecb1afae32e88885b2309dd39f0f161)

## 2. WeChatMsg：原作者历史源码可以保存，不能包装成已验证成品

选定原作者提交 `9457ecdad74826ebede9a040b1d86d986c968f1e`，Git tree 为 `f0ff70068c3ab2ba1592afbb2f684b821d9d0209`。提交明确适配微信 4.0.3；固定配置包含 157 个离散 3.x 条目。它们是历史适配证据，不是对所有 3.x/4.x 的承诺。[LC044，适配提交，2025-04-09](https://github.com/LC044/WeChatMsg/commit/9457ecdad74826ebede9a040b1d86d986c968f1e)、[version_list.json](https://github.com/LC044/WeChatMsg/blob/9457ecdad74826ebede9a040b1d86d986c968f1e/wxManager/decrypt/version_list.json)

可恢复来源包括直接 fork tqjason 的 `14b466dcc4c60b43d9d79301e489c8d6029daed4`，核对只多一个同步工作流；实际归档仍从原作者固定提交取得，不把镜像维护者当作新原作者。根许可在此快照为 MIT，原作者之前已作许可变更，不是由本项目或镜像擅自重新许可。[tqjason，保留快照](https://github.com/tqjason/WeChatMsg/commit/14b466dcc4c60b43d9d79301e489c8d6029daed4)、[LC044，许可变更，2025-03-28](https://github.com/LC044/WeChatMsg/commit/6535ed011c90f4ce5daea6986d420617b14a70f2)、[固定 LICENSE](https://github.com/LC044/WeChatMsg/blob/9457ecdad74826ebede9a040b1d86d986c968f1e/LICENSE)

建议保留 HTML、配套 `.html.json` 与媒体目录，并按消息 ID、时间、显示名、引用和原文上下文定位。不要默认选择 AI 训练 JSON：其对话整理过程不等价于逐条保留证据字段；也不能据显示名补造稳定账号身份。[HTML 导出器](https://github.com/LC044/WeChatMsg/blob/9457ecdad74826ebede9a040b1d86d986c968f1e/exporter/exporter_html.py)、[训练 JSON 导出器](https://github.com/LC044/WeChatMsg/blob/9457ecdad74826ebede9a040b1d86d986c968f1e/exporter/exporter_json.py)

现有源码例程需要参数与依赖配置；`requirements.txt` 未列出所有导出器导入的依赖，例如 Word 导出使用的 python-docx。上游仍排除 Win7 和 macOS。保留源码并不意味着本项目提供新打包器或通用命令行。[LC044，使用说明](https://github.com/LC044/WeChatMsg/blob/9457ecdad74826ebede9a040b1d86d986c968f1e/readme.md)、[导出例程](https://github.com/LC044/WeChatMsg/blob/9457ecdad74826ebede9a040b1d86d986c968f1e/example/3-exporter.py)、[依赖声明](https://github.com/LC044/WeChatMsg/blob/9457ecdad74826ebede9a040b1d86d986c968f1e/requirements.txt)

**为什么不另找一个 EXE 直接推荐：**本次定向查到 evergardener 的打包工作流曾成功，但其 `memotrace-exe` Actions artifact 已过期，未确认持久 Release。另一个声称适配 4.1.10.53 的补丁 fork 缺少完整依赖/配套文件与可核对安装包，不能仅凭声明列为已验证升级。[evergardener，构建记录](https://github.com/evergardener/WeChatMsg/actions/runs/17018784420)、[liyunxiang041012-max，4.1.x 补丁固定提交](https://github.com/liyunxiang041012-max/WeChatMsg-Fix-4.1.x-/commit/f48bb85a8bd87269a86ae2e7e97275aaf2c92e01)

## 3. PyWxDump 与 wechatDataBackup：有可追溯旧存档，不提升为默认

**PyWxDump 3.1.45。**固定提交 `d62e846ff6e90a57999afdc0cc003b599624e8cb` 可由 PwnDexter 直接 fork 保留，Git tree 相同。该快照 LICENSE 为 MIT。固定 `WX_OFFS.json` 有 66 个离散版本，从 3.2.1.154 到 3.9.12.55，无 4.x 条目；固定 FAQ 将支持环境限定在 Windows 10 x64 或更新。[原作者固定快照](https://github.com/xaoyaoo/PyWxDump/tree/d62e846ff6e90a57999afdc0cc003b599624e8cb)、[PwnDexter 同提交](https://github.com/PwnDexter/PyWxDump/tree/d62e846ff6e90a57999afdc0cc003b599624e8cb)、[版本配置](https://github.com/xaoyaoo/PyWxDump/blob/d62e846ff6e90a57999afdc0cc003b599624e8cb/pywxdump/WX_OFFS.json)、[FAQ](https://github.com/xaoyaoo/PyWxDump/blob/d62e846ff6e90a57999afdc0cc003b599624e8cb/doc/FAQ.md)、[LICENSE](https://github.com/xaoyaoo/PyWxDump/blob/d62e846ff6e90a57999afdc0cc003b599624e8cb/LICENSE)

作者对 4.0.3.40 等新版的问题另有说明；当前首页自述收到律师函后撤下代码。这里仅记录作者的项目状态声明，不作法律结论。历史文件仍能取得，不代表当前官方支持或所有新版本可用。[xaoyaoo，版本问题回复](https://github.com/xaoyaoo/PyWxDump/issues/203#issuecomment-2839435786)、[作者当前项目说明，2026-09-03 访问](https://github.com/xaoyaoo/PyWxDump)

**wechatDataBackup 1.2.4。**固定提交 `260c7306adf67963d346f399a483775db47a9107` 日期为 2025-04-15，历史源码声明 Apache-2.0。Gitee 的 main 与 v1.2.4 当次读取均指向同一提交；这能核对内容，不额外证明两个平台的同名账号身份。[原作者历史提交](https://github.com/git-jiadong/wechatDataBackup/commit/260c7306adf67963d346f399a483775db47a9107)、[Gitee 保存来源](https://gitee.com/git-jiadong/wechatDataBackup)、[固定许可证](https://github.com/git-jiadong/wechatDataBackup/blob/260c7306adf67963d346f399a483775db47a9107/LICENSE)

作者在 2025-04-21 仍说明 4.0 适配进行中，晚于这个源码快照；因此没有依据称该存档完整支持 4.x。GitHub 公开的 2026-01-08 Tencent DMCA 通知列到该仓库；公开通知不是法院裁决，但构成再分发和可用性需要注意的背景。本次不增加此项目的源码或二进制副本。[git-jiadong，适配回复](https://github.com/git-jiadong/wechatDataBackup/issues/58#issuecomment-2817723636)、[GitHub，公开 DMCA 通知，2026-01-08](https://github.com/github/dmca/blob/1fd40f947956354b65e5e05e391b86e0f9e81d8d/2026/01/2026-01-08-tencent.md)

## 4. 是否存在更好的其他路线

### WeFlow 5.1.0：平台更广，不等于来源更强

mjkyleo 保存的 v5.1.0 指向 `3c58317af0489f1e31c73d40b8958901d1f57187`，该备份为单个根提交，README 明确说明源码从网络收集。声明的 4.0+ 与多平台发行资产有参考价值，但本次没有恢复出同等连续的原作者提交链，也未验证每个安装包的真实行为。[mjkyleo，固定备份说明，2026-09-02](https://github.com/mjkyleo/weflow/blob/3c58317af0489f1e31c73d40b8958901d1f57187/README.md)、[v5.1.0 发行页](https://github.com/mjkyleo/weflow/releases/tag/v5.1.0)、[根提交](https://github.com/mjkyleo/weflow/commit/3c58317af0489f1e31c73d40b8958901d1f57187)

其 JSON formatter 的 `localId` 为导出序号，保留 `platformMessageId`，但没有 CipherTalk 桌面详细 JSON 的 `rawContent` 字段。因此就“接收原始内容并逐条回查”而言，没有得到全面更优的证据。根许可仍含非商业与相同方式共享要求；本次只登记，不替换主要工具，也不采纳以移除原生授权为卖点的分支。[JsonFormatter.ts](https://github.com/mjkyleo/weflow/blob/3c58317af0489f1e31c73d40b8958901d1f57187/electron/services/export/formatters/JsonFormatter.ts)、[固定 LICENSE](https://github.com/mjkyleo/weflow/blob/3c58317af0489f1e31c73d40b8958901d1f57187/LICENSE)

### WechatExporter：作为 iOS 备份补充，而不是替代桌面工具

BlueMatthew 的 v1.9.5.13 发布于 2022-07-15，固定提交为 `474318a3de729a3c91e9b4f283c3e31982468344`。它处理用户持有的未加密 iPhone/iPad 本地备份，官方历史包面向 Windows/macOS x64；固定说明中的历史测试包括 iOS 15.4 和手机微信 8.0.18，不能外推到现行全部 iOS/微信版本或原生 Apple Silicon 安装包。[BlueMatthew，固定发行版，2022-07-15](https://github.com/BlueMatthew/WechatExporter/releases/tag/v1.9.5.13)、[固定 README](https://github.com/BlueMatthew/WechatExporter/blob/474318a3de729a3c91e9b4f283c3e31982468344/README.md)

该快照 LICENSE 是 Apache-2.0，当前 main 为 GPL-2.0；不能用当前首页许可覆盖旧提交，反过来也不能据旧源码许可对全部发行包作笼统法律保证。HTML 的消息定位来自数据库 `MesLocalID`，不是服务器消息签名。[旧快照 LICENSE](https://github.com/BlueMatthew/WechatExporter/blob/474318a3de729a3c91e9b4f283c3e31982468344/LICENSE)、[许可变更提交，2022-07-15](https://github.com/BlueMatthew/WechatExporter/commit/21165c07103e5e2a508a5db05d1c9319ce93b50f)、[消息读取代码](https://github.com/BlueMatthew/WechatExporter/blob/474318a3de729a3c91e9b4f283c3e31982468344/WechatExporter/core/WechatParser.cpp)

**条件性建议：**当用户已经有合适的 iOS 本地备份时，可以先评估这条路线；不为使用工具而要求取得别人的账号、密钥或备份。本次保留官方发行页入口，未下载或再分发这些安装包。

## 本次实际保存与检查的内容

两个源码包均从 GitHub 官方 codeload 的**完整提交地址**下载，不重新打包。下面的数据来自本地实际读取：

| 源码归档 | 字节数 | 文件数 | 重算结果 |
|---|---:|---:|---|
| CipherTalk-SafeFork `acf221c…` | 39,412,192 | 927 | 所有 Git blobs 组成的 tree 与固定上游 tree 相同；桌面及 CLI 许可副本相同 |
| WeChatMsg `9457ecd…` | 58,035,722 | 264 | 所有 Git blobs 组成的 tree 与固定上游 tree 相同；MIT 许可副本相同 |

可复核证据是 [源码文件与实际 SHA-256](../../importers/README.md)、[完整登记表](../../importers/registry.json) 和 [离线校验器](../../importers/verify_archives.py)。校验器只读归档，不解包或启动源码；检查路径、重复条目、文件类型、展开大小、SHA-256、Git tree 和许可副本。两份文件各自低于 100 MiB，因此源码无需 Git LFS；这不适用于未下载的较大 DMG/EXE。

“完整源码快照”是完整仓库文件快照，不意味着每个依赖均提供源码：WeChatMsg 内有 FFmpeg 可执行文件，CipherTalk 也含预编译依赖。归档保持原字节，未运行其中的工作流、安装脚本、导出器、AGENTS 或 skills；它们不是本项目插件的指令。

本地文本检查覆盖 CipherTalk 的 769 个可解码文本文件和 WeChatMsg 的 113 个可解码文本文件。命中的凭据赋值模式为代码表达式、配置键或占位内容；模型数据中的长数字命中为小数数字片段。本次文本检查未识别出真实凭据。这个范围不等于对剩余二进制、原生依赖、所有图片内容或恶意行为完成审计；也不能据此承诺“绝对安全”。

## 证据缺口、限制与维护建议

- **没有实际导出验收。**未安装或运行 DMG/EXE、历史 Python 工具及 iOS 导出器；没有拿真实微信数据测试。需在用户明确选择的系统、架构和微信版本上另行验收。
- **安装包不是本仓库镜像。**摘要来自上游 API，链接只做可达性检查；签名、源码到二进制的可复现对应、原生依赖来源仍有缺口。上游发生变化时应停止使用旧结论并复核，不自动追随 latest。
- **归档一致性不是作者签名。**SHA-256 和 Git tree 可检测归档与登记快照的差异，但不能证明作者身份、登记表本身未被篡改或第三方项目无恶意行为；应同时审查本仓库变更历史。
- **权利需要按版本与对象区分。**这是许可证与项目状态的事实整理，不是完整法律意见；桌面/CLI、原项目/依赖、工具/聊天内容都不能混用授权。
- **研究范围有边界。**本次优先原作者仓库、固定历史提交、可比较的 forks、Release/API、构建日志和作者回复；社区声明仅作为待核线索。通用搜索工具的访问曾失败，关键证据改以 GitHub API、原始固定文件和 Gitee 公开 refs 取得；不能声称覆盖所有私人分发包或互联网镜像。
- **停止理由。**指定四个项目与两个实质不同的替代路线已有可追溯版本和明确处置；后续找到的补丁/打包分支没有消除来源链或运行验证缺口。继续泛搜不太可能改变本次“两个源码存档 + 上游下载入口”的决策，未解决项目已保留为条件而非包装成结论。

以后只有在取得更强的来源链、精确兼容性证据、持久发行资产或更完整原始导出契约时，再评估升级。版本目录应新增而非覆盖；先校验来源与许可，再更新登记表、入口和相关引用。本轮不创建新的聊天解析接口或自动追踪上游版本的任务。
