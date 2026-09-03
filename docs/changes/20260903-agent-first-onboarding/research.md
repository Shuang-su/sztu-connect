# Agent-first onboarding 研究依据

日期：2026-09-03。研究为本轮批准计划的基础；实施细节及验证结果另见 [完成记录](completion.md)。完整来源、对应论断与证据缺口保存在 [sources.json](sources.json)，完整批准计划见 [plan.md](plan.md)。

## 研究问题与范围

面向已有一种可用本地 Agent、但不熟悉 Python 或 Git 命令的记录者，研究能否通过一句话完成 SZTU Connect 的环境准备、适用工具配置、隔离示例与首次记录交接。研究不包含网站部署、RAG 服务、自动同步或九种客户端统一市场插件。

研究按四步完成：核对本地项目现状；寻找 Agent 友好项目的一手安装文档；按客户端官方文档核实入口与执行环境差异；明确本地优先、工具依赖和实际验收边界。只读研究阶段未安装软件、登录账号或修改远端，随后用户明确批准本地实施。

## 可采用的结构

| 来源 | 可采用的方法 | 不带入本项目的行为 |
|---|---|---|
| [Agent Reach 安装指南](https://github.com/Panniantong/Agent-Reach/blob/da5044d26fc6adddb6554d5679c94ac22e76e428/docs/install.md) | 人的一句话入口指向 Agent 的详细安装指南；检查依赖并给出就绪状态 | 账号 Cookie 工作流、全局安装范围、固定耗时承诺 |
| [Superpowers 安装说明](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/README.md#installation) | 不同客户端分别说明原生接入方式，同时保留直接读取指南的入口 | 过时版本的导入路径，或把所有客户端当作同一种插件宿主 |
| [gstack README](https://github.com/garrytan/gstack/blob/0d1bd5616c0ef096bb7ccee336f63c60ee408618/README.md#install--30-seconds) | 自然语言安装、可执行助手与第一次实际使用连续衔接 | 自动更新、自动提交与特定浏览器路由 |

这是一组文档与流程设计参考，不表示引入上述项目的实现代码或依赖。

## 客户端差异与证据

- Claude Code 不直接把 `AGENTS.md` 当作自动入口，采用薄的 `CLAUDE.md` 导入。[Anthropic 文档](https://code.claude.com/docs/en/memory)
- Codex 的项目指令、Skill 和插件属于不同的发现层；安装插件不等于给用户工作副本准备 Python。[项目指令](https://learn.chatgpt.com/docs/agent-configuration/agents-md)、[插件](https://learn.chatgpt.com/docs/plugins)
- WorkBuddy 需要本地工作空间和可执行任务的模式；未找到足以承诺 `AGENTS.md` 自动加载的依据，保留显式读取。[任务文档](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Task-Bar)
- DeepSeek Harness 是官方 `dsh` Developer Preview，可读项目指令，但不支持把 `@path` 当作导入语法；入口保留实验标记。[官方介绍](https://www.deepseek.com/harness/en/)、[指令实现说明](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/context/agent-instructions/README.md)
- Kimi Code 的本地 CLI 和标准 Skill 可复用本项目说明；不使用客户端 `/init` 覆盖已有规则。[快速上手](https://www.kimi.ai/zh-hans/help/kimi-code/cli-getting-started)、[Skill 文档](https://moonshotai.github.io/kimi-code/en/customization/skills)
- ZCode 的规则以当前工作区根文件为范围，不假定递归加载或导入；无项目会话的接续需要明确切换任务。[官方说明](https://zcode.z.ai/en/docs/agents)
- Cursor 本地 Agent 可操作文件和命令并使用 `AGENTS.md`；问答模式和云端任务不等同于本机初始化。[规则](https://cursor.com/docs/rules)、[Agent](https://cursor.com/docs/agent/overview)
- TraeWork 的 Windows Work / Design 是隔离环境，安装宿主机工具使用 Code 模式；规则导入需要启用设置。[沙箱](https://docs.trae.cn/work_sandbox)、[规则](https://docs.trae.cn/work_rules)
- QoderWork 以用户授权的 Working Folder 和 GitHub Skill 入口为依据；未把 Qoder CLI 的规则发现机制套用到此产品，实际命令与宿主机路径映射需在运行时验证。[文件管理](https://docs.qoder.com/qoderwork/file-management)、[Skill](https://docs.qoder.com/qoderwork/skills)

## 项目约束核对

研究基准为 `eb30c774db2f76752a0ed6d9da02ee42d6aeac11`：没有 bootstrap 命令，`doctor` 只检查部分项目文件和 Python；CI 是 Ubuntu，实际仓库测试强制断言 Event 数量为零。实施开始时重新核对工作树、基准和 53 项原有测试。

研究时，附带工具任务的独立工作副本已有 `importers/registry.json` 草稿，但尚未进入实施分支。初版仅据其已观察到的 `schema_version: 1` 结构制作适配与合成测试，没有复制另一任务的未完成文件或自行替换工具。

实施期间，该任务正式交付进入 `main`（`621de40f2fed1d2345b2e8bff1d7797962072150`），并以本地合并 `9628c8b81dc6a2d34859d3a93478ff2675a9ac50` 集成到本轮分支。最终清单使用普通 Git 保存两份源码，不使用 LFS；另登记 CipherTalk 的 macOS arm64 / Windows x64 固定上游安装包。离线归档校验和正式清单选择回归通过；实际安装包及应用运行仍未验收，不能由源码哈希推断为已安装或安全。

GitHub 是可选后续步骤；浏览器授权属于用户操作。Fork 默认行为可能影响远端命名，因此在流程中显式保留现有映射，并使用不克隆、不添加远端的参数取得 Fork，再读回确认。[登录说明](https://cli.github.com/manual/gh_auth_login)、[Fork 说明](https://cli.github.com/manual/gh_repo_fork)

## 证据缺口与停止条件

一手文档足以确定共用指南、薄适配、宿主环境确认和本地初始化助手的设计；继续搜索无法替代实机安装。正式工具清单与源码交付这一依赖已解决；剩余缺口是实际应用安装 / 启动、真实 Windows 运行、九客户端版本与模式逐项验收，以及指南进入默认分支后的公开 URL 检查。它们在 [验收矩阵](../../ONBOARDING_TEST_MATRIX.md) 中保持未完成状态，不由静态兼容性推断为已支持。`sources.json` 的 `gaps` 保留批准计划时的证据快照，后续进展单列在 `implementation_updates`。
