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

## 未完成与边界

- 本分支没有正式 `importers/registry.json` 和工具文件，工具阶段为 `registry_pending`。已核对清单草稿结构并以合成夹具测试；未安装或启动真实聊天应用，未访问数据库、聊天账号或 Computer History。
- Windows / macOS 初始化 CI 已配置，但未推送，因此新增远端作业尚未运行；Windows 实机和九种客户端的完整端到端体验均保持待验证，见 [验收矩阵](../../ONBOARDING_TEST_MATRIX.md)。
- 指南公开 URL 需要文档进入默认分支后再验证；本地文件存在不表示远端链接已发布。
- 没有改动数据模型、导出格式、内容校验策略或正式内容；没有发布网站、RAG 服务、PR、Release 或其他远端产物。
- 本地日志和示例位于 Git 忽略目录，不纳入提交；用户已有工作副本和另一工具归档任务的未提交内容未被覆盖。

## Checkpoint

- `1a3e381226542b5a1a907b77a25e69cf15b1bf63` — `feat(onboarding): add resumable local bootstrap helper`，初始化助手、行为与边界测试、空骨架夹具修正、Windows / macOS CI。
- 文档及薄适配入口随后单独提交；最终回复和后续完成记录会给出 SHA。

实施期间，上游工具归档任务在独立工作副本完成并进入 main（`621de40`）。将在当前实施分支合入这项已批准依赖，保留其来源记录和双方改动，再补充集成验证；不改动或推送 main。
