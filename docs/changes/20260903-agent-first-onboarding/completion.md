# 多 Agent 一句话开始：完成记录

日期：2026-09-03。实施分支：`codex/agent-first-onboarding`。起点：`eb30c774db2f76752a0ed6d9da02ee42d6aeac11`，开始时工作树干净。完整请求见 [request.md](request.md)，批准计划见 [plan.md](plan.md)，研究及证据缺口见 [research.md](research.md) 与 [sources.json](sources.json)。

## 已实现

- README 快速开始以自然语言初始化请求为首要入口，按结果、首条记录、按需 GitHub、折叠开发者命令组织；现有品牌、诗文、材料说明与顺序保留。
- `docs/GETTING_STARTED.md` 是九种客户端共用的唯一详细指南；`AGENTS.md`、薄的 `CLAUDE.md`、`setup-sztu-connect` Skill 与插件初始化提示只负责路由。
- 纯标准库 `scripts/bootstrap.py` 检查工作副本和实际 Git / Python，准备隔离虚拟环境、锁定依赖与 CLI；按平台适配固定工具清单、校验 LFS 实体 / SHA-256、缓存固定下载，并报告安装元数据。
- 隔离最小 / 聊天示例写入 `.work/onboarding/`；复用已有 CLI 做校验、双构建比较、知识 JSONL 导出和聊天 HTML。重复运行复用通过验证的状态，用户改动或不明文件保持原样。
- `--check` 只读；额外 `--github` 仅在请求时读取 GitHub 授权与上游写权限，返回分支 / Fork 建议，不更改远端或账号。
- 测试将“正式事件必须为空”限定为专用夹具；增加核心 bootstrap 的行为 / 失败 / 边界测试、文档链接测试，以及 macOS / Windows CI 作业，保留原 Linux 作业。

## 第一轮本地验证

实施前的 53 项原有测试通过。本地 macOS 15.5（24F74）/ arm64、Python 3.13.5、Git 2.49.0 已完成全新工作副本的锁定依赖安装、示例生成、重复运行、只读无写入与中断恢复测试。包含 opt-in 核心集成的全套 **93 项测试通过**；两次构建的 12 个派生文件哈希相同，正式内容与数据无差异。

`doctor`、`validate --json`、`privacy-scan --json`、`build --json`、`check --json`、编译检查、两份 JSON 格式检查和 `git diff --check` 通过。初始化 Skill 和整个插件通过各自提供的结构校验器；CI YAML、Skill UI 元数据及跨文件链接 / 锚点通过检查。

README 正文通过 GitHub Markdown API 的 GFM 渲染，在临时本地预览中核对快速开始、完整复制提示词和开发者折叠区的实际展开行为；保留两个表格和结尾文案。预览使用本地样式与锚点外壳，不是已发布的默认分支页面，未把公开指南 URL 报为可用。验收后关闭临时浏览页与仅绑定回环地址的预览服务。

一次完整测试暴露 macOS Finder 自动生成 `.DS_Store` 导致只读快照误报；中断昂贵的整文件差异输出后，把快照比较改为文件哈希 + 修改时间，仅排除这一系统元数据文件。保留对项目文件和状态输出的完整无写入检查，重跑 93 项全部通过。验证脚本需要的 PyYAML 6.0.3 仅安装在忽略的临时工具环境，不改项目锁文件或全局 Python。

独立 Skill 只读演练：读取 Skill、共用指南及项目规则，运行 `bootstrap --check --json` 与只读 `doctor`；没有安装、构建、登录或修改工作树。能正确区分运行时已可用、当前指纹示例未生成和工具清单缺失，未把只读请求升级为安装。该演练不是九种客户端的完整安装验收。

## 正式工具依赖集成与复验

先提交初始化助手与文档两个 checkpoint，再将工具归档任务正式交付的 `621de40f2fed1d2345b2e8bff1d7797962072150` 合入本轮实施分支。处理了 CI、README 项目树、聊天 Skill 和记录 Skill 四处重叠：保留双方检查、工具来源与聊天证据流程，仅衔接到共用初始化入口，没有改写对方已经交付的源码或许可。此操作是实施分支吸收依赖，不是将本轮功能合并或推送到 `main`。

两份固定源码存档通过 `python importers/verify_archives.py` 的离线 SHA-256、Git tree / blob 和许可校验，没有执行上游源码。工具任务新增的 14 项测试与本轮测试合计 107 项通过；随后补充正式清单的平台选择 / 无下载和无回执输出保护两项回归，完整 **109 项测试通过**（含真实核心环境集成）。核对 macOS arm64 与 Windows x64 均选择清单中的 CipherTalk 固定版本，不把 WeChatMsg 源码备份或 catalog-only 条目标成已安装。

指南同步反映正式交付：源码使用普通 Git，当前不需要 LFS；安装包从清单固定的上游地址按平台获取。LFS 指针保护保留为兼容检查，不为当前仓库引入 LFS。

最终边界复核对照本地 pip 实现，隔离可能重定向安装解释器、根目录、源码、构建状态和详细日志的继承环境变量。真实集成夹具故意设置工作副本之外的临时目标，仍能完成初始化且该目标没有被创建；没有修改用户的全局环境或 pip 配置。已有示例输出但缺少验收回执时返回 `unverified_outputs / pending_user`，保留文件并要求核对恢复方式，不把它们猜成可覆盖的中断产物。

在实际工作副本中单独生成更新指纹 `5000e42b5aa1c92f` 的隔离示例，再执行只读 bootstrap：`workspace`、`runtime`、`example` 为 `completed`，`local_ready: true`；工具为 `pending_user / missing_payload`，GitHub 为 `not_applicable / local_only`，`operations` 为空。没有因这次实现验证而下载或安装真实聊天应用。聊天 HTML 已在仅绑定回环地址的本地浏览器预览，标题、两条合成消息与回复标识正常，未见页面错误日志；示例关联及 `claim-example-purpose → source-example-documentation` 引用已核对。预览后关闭临时标签页与服务。

相对已集成上游 `621de40` 的本轮变更通过 `git diff --check`。合并阶段检查曾报告 CipherTalk 上游许可原文的 4 行尾随空格；按原始字节归档要求保留，不通过改写第三方许可掩盖差异。

最终复验：两份项目 JSON、变更证据 JSON、编译检查、`doctor`、`validate`、`privacy-scan`、`check` 与双次 `build` 通过，12 个派生文件逐个 SHA-256 相同。隐私扫描的 `block: 0 / review: 6` 与工具交付边界一致：两份未作文本扫描的源码压缩包、三份非标准扩展名许可文本及工具研究记录中的 CI run ID 样式提示；没有改动扫描器来消除提示。相对 `621de40` 的 `src/`、Schema、正式内容、派生数据、依赖锁及 `importers/` 均无差异。最终 README 再次通过 GitHub Markdown API 渲染，完整复制提示词、两个折叠区和两个表格均保留；没有将渲染 API 当作发布操作。

## 未完成与边界

- 正式工具清单和源码归档已集成，但图形安装包在本机未下载 / 校验，真实应用未安装或启动；工具状态准确保持待完成。源码归档与哈希不是安全审计或真实应用体验证明；未访问数据库、聊天账号或 Computer History。
- Windows / macOS 初始化 CI 已配置，但未推送，因此新增远端作业尚未运行；Windows 实机和九种客户端的完整端到端体验均保持待验证，见 [验收矩阵](../../ONBOARDING_TEST_MATRIX.md)。
- 指南公开 URL 需要文档进入默认分支后再验证；本地文件存在不表示远端链接已发布。
- 没有改动数据模型、导出格式、内容校验策略或正式内容；没有发布网站、RAG 服务、PR、Release 或其他远端产物。
- 本地日志和示例位于 Git 忽略目录，不纳入提交；用户已有工作副本和另一工具归档任务的未提交内容未被覆盖。

## Checkpoint

- `1a3e381226542b5a1a907b77a25e69cf15b1bf63` — `feat(onboarding): add resumable local bootstrap helper`，初始化助手、行为与边界测试、空骨架夹具修正、Windows / macOS CI。
- `2544a4ef6bc02eae1ac4a5ddacfcfe419f7fc92b` — `docs(onboarding): add shared agent-first getting started flow`，共用指南、README、薄适配入口、研究 / 请求 / 计划和首轮完成记录。
- `9628c8b81dc6a2d34859d3a93478ff2675a9ac50` — `merge: integrate verified chat tool archive dependency`，将已完成工具任务的正式交付合入本地实施分支，保留上游历史和双方行为。
- `d9e7cd1ebc43d62ff286c0018d87d3b8851431bc` — `fix(onboarding): preserve local install and example boundaries`，补齐继承环境变量和无回执输出的保护，验证正式工具清单，109 项测试通过。
- 交付说明校准、最终验收状态及本完成记录随最后文档 checkpoint 提交；该提交 SHA 在最终回复中报告，避免文档自引用自身尚未生成的 SHA。
