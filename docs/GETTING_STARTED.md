# 开始使用 SZTU Connect

这份指南同时面向记录者和替记录者操作电脑的 Agent。你只需要一种能读写本地文件、执行命令的客户端；不需要先学会 Python、Git 或安装本项目插件。

**先在本地跑通，再按需连接 GitHub。** 这里的“初始化”是准备本地工作副本、环境、适用工具和示例，不是部署网站，也不包括自动收集聊天、Computer History 活动或发布记录。

[选择客户端](#选择客户端) · [Agent 执行流程](#agent-执行流程) · [继续初始化与故障恢复](#继续初始化与故障恢复) · [需要时连接 GitHub](#需要时连接-github) · [完成判定](#完成判定)

## 选择客户端

打开一个本地工作区或授权的工作文件夹，把 [README 的一句话入口](../README.md#快速开始) 发给 Agent。以下是文档核对后的接入方式，不等于九种客户端都已通过真实安装验收；版本、平台和执行模式的实测状态见 [验收记录](ONBOARDING_TEST_MATRIX.md)。

| 客户端 | 从哪里开始 | 项目指引如何进入上下文 |
|---|---|---|
| Claude Code | 在本地项目中执行任务 | 根 `CLAUDE.md` 导入 `AGENTS.md`；不能假定自动读取 `AGENTS.md`。[官方说明](https://code.claude.com/docs/en/memory) |
| WorkBuddy | 选择本地工作空间，使用 Craft 执行模式，或确认计划后执行 | 显式读取本指南；原生 Skill 导入是可选便利入口，不假定自动读取 `AGENTS.md`。[任务说明](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Task-Bar)、[Skill 说明](https://open.workbuddy.cn/en/docs/skill) |
| Codex | 打开本地项目；未装项目插件也可开始 | 读取根 `AGENTS.md`；装有项目插件时可用 `setup-sztu-connect` Skill。[项目指令](https://learn.chatgpt.com/docs/agent-configuration/agents-md)、[插件说明](https://learn.chatgpt.com/docs/plugins) |
| DeepSeek Harness | 使用官方 `dsh` 的本地工作区和文件、命令工具 | 显式读取本指南，可复用项目指令，但不依赖 `@path` 导入。Developer Preview，作为实验入口。[介绍](https://www.deepseek.com/harness/en/)、[指令加载](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/context/agent-instructions/README.md) |
| Kimi Code | 使用本地 CLI 会话 | 显式读取本指南，可复用标准 Skill；不要用客户端 `/init` 覆盖项目规则。[快速上手](https://www.kimi.ai/zh-hans/help/kimi-code/cli-getting-started)、[Skill 说明](https://moonshotai.github.io/kimi-code/en/customization/skills) |
| ZCode | 先选择项目工作区，再发送任务 | 使用当前工作区根 `AGENTS.md`，不假定递归加载或 `@import`。无项目会话不能直接转为项目会话时，新建项目任务并接续。[官方说明](https://zcode.z.ai/en/docs/agents) |
| Cursor | 在本地项目使用 Agent，而非仅问答或云端任务 | 复用根 `AGENTS.md`，显式读取本指南。[规则](https://cursor.com/docs/rules)、[Agent](https://cursor.com/docs/agent/overview) |
| TraeWork | 桌面本地任务；Windows 安装宿主机环境时选 Code 模式 | Windows 的 Work / Design 使用隔离虚拟环境；自动加载 `AGENTS.md` 需启用官方导入开关，未启用时显式读取。[沙箱](https://docs.trae.cn/work_sandbox)、[规则](https://docs.trae.cn/work_rules) |
| QoderWork | 选择并授权 Working Folder，先确认命令实际运行的位置 | 显式读取本指南，或按官方方式导入 GitHub Skill 链接；不套用 Qoder CLI 的规则发现机制。[Skill](https://docs.qoder.com/qoderwork/skills)、[文件管理](https://docs.qoder.com/qoderwork/file-management) |

根 `skills/` 是本项目工作流的唯一来源。没有原生 Skill 发现能力的客户端可以直接读取其中的 `SKILL.md`，不需要生成九份不同规则。不要运行客户端自己的 `/init` 来重新生成 `AGENTS.md` 或 `CLAUDE.md`。

如果刚更换了工作区、启用了规则导入或刷新了 Skill，请重新打开该项目任务，并发送：“请在当前工作副本读取 `AGENTS.md` 和 `docs/GETTING_STARTED.md`，继续初始化。”不能只在旧会话中执行 `cd` 就假定所有客户端都重新加载了指令。

## Agent 执行流程

读完本节再开始执行。复用用户已经提供的客户端、目标目录与选择，只询问尚未明确、会影响文件或系统的决定。系统安装、权限提示和账号验证由用户处理；遇到授权窗口时说明需要哪一步，等待后从已有状态继续。

### 1. 确认本机与工作副本

1. 确认客户端名称、版本、执行模式、操作系统、架构、工作目录和写入权限。把客户端显示的工作文件夹与命令实际返回的路径对应起来；WSL、容器、云端任务或沙箱不自动等于宿主机。不能确认时，先引导切换到本地模式，不在未知环境里安装。
2. 用户已经打开完整的 SZTU Connect 工作副本时，先检查 `git status --short --branch`、`git remote -v`、`git rev-parse --show-toplevel` 和根 `AGENTS.md`。保留当前分支、未提交内容和既有远端；不要自动拉取、切分支或重新克隆覆盖它。
3. 还没有工作副本时，在用户选定的父目录下选择独立的 `sztu-connect` 目录，用公开 HTTPS 地址 `https://github.com/Shuang-su/sztu-connect.git` 克隆，不要求 GitHub 登录。非空目录若不是正确副本，停止并请用户选择新目录。当前源码存档使用普通 Git，clone 会包含这些文件；先检查目标卷空间，不需要 Git LFS。只有所选版本确实使用 LFS 时，才在该次 clone 进程设置 `GIT_LFS_SKIP_SMUDGE=1`，避免取用不适用平台的大文件，不修改全局配置。
4. 缺少 Git 时先完成下一节的 Git 准备，再克隆。克隆后读取根 `AGENTS.md` 与本地本指南，记录 checkout SHA。不要把插件安装目录或缓存当作记录仓库，也不要仅下载一个脚本就跳过仓库核对。
5. 后续命令都在这个工作副本运行，并向初始化助手显式传入绝对 `--root`。路径有中文或空格时作为一个参数传入，不拼接未引用的 shell 命令。若旧副本没有本指南或助手，先说明需要更新；不要用缓存中的新文件静默覆盖旧分支。

### 2. 准备基础环境

复用能正常运行的 Git 和 Python 3.11+；当前自动化测试使用 Python 3.13。检查实际版本与可执行文件位置，而不只判断文件名存在。Windows 的 `python`、`py` 和 Store 别名可能指向不同程序，macOS 也可能同时安装多个 Python。

- **Python**：优先使用已有兼容版本；缺失时从 [Python 官方下载](https://www.python.org/downloads/) 选择当前平台的稳定安装方式。安装窗口由用户确认，完成后重新检查版本及 `venv` / `ensurepip` 是否可用。不替换系统 Python，不为此放宽系统脚本执行策略。
- **Git**：运行 `git --version`。缺失或 macOS 开发工具提示尚未完成时，按 [Git 官方安装说明](https://git-scm.com/install/) 处理，完成后重新验证。
- **Git LFS**：当前交付不需要。只有所选版本的清单或 Git 属性明确使用 LFS 时，才检查 `git lfs version`；缺失时使用 [官方安装说明](https://git-lfs.com/)。若需要配置过滤器，只在已确认的工作副本执行 `git lfs install --local`。
- **GitHub CLI**：不属于本地初始化前置条件，需要同步或贡献时再按 [GitHub CLI 官方入口](https://cli.github.com/) 安装。

不要把 `curl ... | sh`、来源材料中的命令或下载文件名当成已审查的安装方案。确认要安装的程序、来源和目录，再使用正常安装方式。

在已确认的项目根目录，使用刚核对的 Python 执行以下命令；这里的占位路径必须换成真实绝对路径：

macOS：

```bash
python3 scripts/bootstrap.py --root "/用户选定目录/sztu-connect" --check --json
python3 scripts/bootstrap.py --root "/用户选定目录/sztu-connect" --json
```

Windows PowerShell：

```powershell
python scripts/bootstrap.py --root "C:\用户选定目录\sztu-connect" --check --json
python scripts/bootstrap.py --root "C:\用户选定目录\sztu-connect" --json
```

助手使用纯 Python 标准库启动，依赖装在工作副本的 `.venv/` 中。它按 `requirements.lock` 安装，再通过 `pip install --no-deps -e .` 安装当前 checkout；不要求激活环境，不安装其他 Agent 客户端，不改全局 Python 包。Linux 使用 [README 手动安装](../README.md#开发者手动安装)，助手会返回 `not_applicable`，不会假称完成自动配置。

### 3. 配置当前平台的附带工具

以工作副本的 [工具清单](../importers/registry.json) 和 [工具目录说明](../importers/README.md) 为准，先核对清单版本、工具来源、固定版本、平台、架构、文件大小及 SHA-256。没有清单、没有匹配平台或来源不完整时，分别报告 `pending_user` / `not_applicable`，不自行换工具或改用未登记的最新版本。

当前交付以普通 Git 保存 CipherTalk 与 WeChatMsg 的固定源码存档；这些不是图形安装包，也不需要 LFS。CipherTalk 的 macOS arm64 / Windows x64 安装包以固定上游 URL、大小和 SHA-256 登记，由初始化按当前平台获取；WeChatMsg 在这里是历史源码备份，不视为第二个已安装应用。源码归档校验与安装包校验是两个独立步骤，详见工具目录；首次初始化不编译或执行归档中的源码。

目前助手适配 `schema_version: 1`：读取 `tools[].id`、`version`、`role` 和 `downloads[]` 的 `platform`、`arch`、`filename`、`size_bytes`、`sha256`、`url`；可选 `path` 是相对 `importers/` 的归档路径。未知版本或多份匹配安装包需要人工核对，不猜测。

- `--check` 只核对现状，不下载。正常初始化复用已通过校验的归档实体；缺少实体或只有 Git LFS 指针时，按清单中的固定 HTTPS 地址下载相同字节到 `.codex-work/downloads/onboarding/<工具>/<版本>/`。
- 如果所选版本确实使用 LFS 且需要补齐仓库实体，先检查 LFS 配置与空间，再只拉取已选平台对应的路径。核对真实文件大小和 SHA-256；以 `version https://git-lfs.github.com/spec/v1` 开头的文本不是安装包。缓存中的同哈希文件可用于安装，但不表示仓库的 LFS 指针已经补齐。
- 下载内容验证通过前不会作为安装包保留；已存在但哈希错误的文件不会被覆盖或运行。不要把下载成功、LFS 下载成功或 SHA-256 一致当作安全认证。
- 清单中的 `catalog-only-*` 条目只是参考目录；源码备份也不等于可安装应用。助手不会从源码自动编译或顺带安装其他工具。
- 取得已验证安装包后，Agent 按随档说明执行当前系统的正常安装流程。系统授权、安装窗口和升级已有应用的选择交给用户，不关闭 Gatekeeper、安全软件或修改执行策略来跳过提示。不要自动打开数据库、登录聊天账号、导出记录或提取账号材料。
- 安装结束后核对**实际应用位置、产品名称和版本**，再重新运行检查。不能只凭 DMG / EXE 文件存在就宣布已安装。助手能识别标准位置的 CipherTalk 应用元数据；自定义位置、不同产品命名或缺少版本信息时保持待核对，不编造完成状态。应用能否实际启动另由 Agent / 用户确认，首次启动不能顺带授权数据访问。

助手不会自动运行图形安装器。工具阶段停在 `pending_user` 时，Agent 应执行上述正常安装或等待必要授权，而不是结束为“全部完成”；如果归档交付缺失，可明确说明依赖，让用户先使用核心示例，后续重复运行补齐。

### 4. 跑通隔离示例

核心环境就绪后，助手在 `.work/onboarding/examples/<内容指纹>/` 建立独立示例副本，复用 [最小示例](../examples/minimal/) 和 [聊天结构示例](../examples/chat/messages.example.jsonl)，依次运行：

- `doctor`、`validate`、`privacy-scan` 和 `validate-chat`；
- 两次 `build`，逐文件比较生成结果；
- `export-knowledge` 和 `render-chat`。

示例输出包含时间线、反向链接、目录、知识 JSONL 和聊天 HTML；具体绝对路径在结果的 `stages.example` 中。用客户端的文件预览打开 HTML，并展示至少一条示例关联和一条来源引用。没有图形预览时给出可打开的本地文件路径，说明尚未完成视觉验收。

这些是结构演示，不是真实校园史料，不复制进正式 `content/` 或 `sources/records/`。已有正式记录不必为空，助手不会为获得“空骨架”而删除它们。示例或程序更新时使用新的内容指纹目录；已被用户修改的现有示例输入、已验收输出会报告冲突，不覆盖。

### 5. 带用户记录第一件事

展示项目目录与可用结果后，请用户提供“发生了什么、什么时候发生、有什么材料”。读取根 `AGENTS.md` 要求的内容规范和 `skills/record-campus-event/SKILL.md`，再请 Agent 整理第一条记录。

这是接下来的内容任务，不是初始化脚本自动替用户填写的测试事件。先检查既有记录与来源，不猜日期或身份。核对每条论断的来源、公开范围、关联与不确定性，确认后运行工作副本的 `sztu-connect check --json`。材料和可复制提示词见 [README](../README.md#准备一条记录)。

聊天导出按 [聊天说明](CHAT_IMPORT.md) 单独发起。Computer History 只在客户端已启用、用户明确指定用途与范围时作为可选线索；本次初始化不会启动采集或导入历史。

## 继续初始化与故障恢复

再次运行同一条命令即可继续；不要清空 `.venv/`、`.work/` 或重新克隆来掩盖错误。助手会重新检查实际文件和版本，复用有效环境、已验证安装包及完整示例，只补未完成部分。

| 情况 | 接续方法 |
|---|---|
| 没有 Python / 版本不足 | 按官方入口安装兼容版本，重新打开命令环境并确认路径，再运行助手。Python 尚不存在时不可能先运行 Python 助手。 |
| `.venv` 是其他目录、旧 Python、缺少解释器，或使用全局包 | 保留目录并说明冲突；经用户确认另选工作副本，或备份、迁移该环境。助手不会删除或覆盖不明环境。 |
| 下载、pip 安装失败或被中断 | 检查网络、可用磁盘和包索引；修复后重跑。失败日志只保留阶段与退出码，不保存可能带凭据的完整命令输出。 |
| 清单缺失、平台无安装包、哈希不匹配 | 分别报告依赖、平台不适用或校验失败；保持原文件，不更换版本，不声称安装成功。 |
| 操作系统安装窗口 / 授权未完成 | 说明正在等待的具体操作。用户完成后重新核对实际应用和版本，再继续。 |
| 路径越界、符号链接 / Windows junction | 停止相关写入，指出具体目录；由用户选择真实目录或检查已有链接，不自动删链接。 |
| 示例只生成了一部分 | 输入未改变、已有验收回执可核对输出时，重跑补齐缺失结果；已有用户改动或输出存在但缺少回执时，保留现场并请用户确认恢复方式，不猜测这些文件的来源。 |
| 客户端更新后不再发现 Skill | 重新打开工作副本、按客户端方式刷新入口；始终可以显式读取本指南继续，不重建项目规则。 |

`--check` 不安装、不下载、不构建、不创建或更新状态文件；它会启动现有解释器做只读版本和校验检查。正常模式把阶段结果写在 `.work/onboarding/status.json`，pip 缓存写在 `.codex-work/cache/onboarding-pip/`。这些目录被 Git 忽略，不应提交。

结果采用与 CLI 相同风格的 JSON envelope：`operation: bootstrap`，详细信息在 `data`。本助手不改动事件或知识导出契约。

| 字段 / 状态 | 含义 |
|---|---|
| `completed` | 对应阶段已通过可执行检查；工具项会注明是安装元数据验证还是实际启动验证。 |
| `pending_user` | 等待用户操作、缺失依赖或尚未完成的步骤。 |
| `failed` | 检查、安装、下载或输出边界失败，须处理后重试。 |
| `not_applicable` | 该平台 / 当前需求不适用，不是“已经安装”。 |
| `local_ready: true` | 工作副本、核心环境与隔离示例可用；工具和 GitHub 仍须各看自身状态。 |
| `ok: true` | 助手要求的阶段均完成或不适用；不代表图形客户端和工具启动均已人工验收。 |
| `host_environment: requires_agent_confirmation` | 助手不能凭 Python 进程证明自己在宿主机，仍需 Agent 核对实际执行模式。 |

退出码为 `0`（上述自动检查完成）、`1`（待操作或平台不适用）、`2`（失败）。不要用 `|| true` 吞掉状态，也不要因为工具未就绪就把已经可用的本地核心说成全部失败。

## 需要时连接 GitHub

只在用户要求同步或贡献时执行本节。本地初始化不检查账号，不创建仓库，不修改远端，也不推送。

1. 检查 GitHub CLI 是否可用，然后核对 `gh auth status --hostname github.com`。已有有效授权就复用；失败先区分网络问题和确实未登录，不擅自退出其他账号。
2. 需要登录时使用浏览器流程 `gh auth login --hostname github.com --git-protocol https --web`，由用户完成验证。不要求把 Token 贴入聊天，也不把授权输出存入项目日志。[官方登录说明](https://cli.github.com/manual/gh_auth_login)
3. 核对 `git remote -v`、目标仓库和当前账号的权限。可选运行 `python scripts/bootstrap.py --root "<真实路径>" --check --github --json`：这个额外开关仅查询上游 `Shuang-su/sztu-connect` 的权限，返回 `branch` / `fork` / `check_permissions` 建议，不创建远端或证明其他仓库的权限。目标不是该上游时，Agent 应单独读取目标仓库权限。
4. 有写权限，在确认的工作副本使用工作分支；没有写权限，先查找当前账号已有 Fork。确需新建 Fork 时，在同步 / 贡献请求的范围内确认目标所有者，用 `gh repo fork Shuang-su/sztu-connect --clone=false --remote=false` 创建，随后读回结果确认。不要重复建 Fork，也不要让默认参数自动重命名 `origin`。[Fork 文档](https://cli.github.com/manual/gh_repo_fork)
5. 保留现有 `origin`、`upstream`。优先按明确的远端名或目标 URL 操作，添加新远端前检查名字是否占用；修改或替换已有远端必须先确认。明确区分个人 Fork 和项目上游。
6. 报告准备提交的文件、目标分支与仓库；commit、push、PR、merge 按当前用户要求及项目规则分别处理。初始化及浏览器授权不是自动发布许可。

## 完成判定

交付时说明客户端版本、系统与执行模式，并分别报告：

- **基础环境**：工作副本位置、checkout SHA、Python / Git 的实际版本、CLI 是否可用；
- **附带工具**：清单版本、平台、payload 校验、实际应用位置和版本、是否真正启动验证；无法完成时列出具体依赖或用户操作；
- **示例**：可打开的 HTML、时间线、反向链接和知识 JSONL 路径；两次构建是否一致；
- **GitHub**：本地模式下为不需要；用户要求连接时再报告授权和权限分支，不展示账号秘密；
- **继续使用**：重新打开同一工作副本后如何继续，以及第一条记录需要用户提供的材料。

没有完成安装窗口、工具只下载了安装包、仅在隔离系统中成功、或只确认了文档格式，都不能写成“本机全部部署成功”。当前版本没有网站、RAG 检索 / 问答、MCP / WebMCP 服务或自动发布能力。
