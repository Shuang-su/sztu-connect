# 用户请求

本记录只包含本轮 Agent-first onboarding 的请求，按收到顺序保留。先前 README 品牌、内容校验和工具归档任务的请求不在本轮重做。

## 最初需求

我们的快速开始目前还是针对开发用户，有没有可能有用户直接可以通过codex、cc、workbuddy直接开始这个项目呢，我们的引导没有针对这部分优化，首先应该是通过一句话部署我们的项目，然后agent根据我们项目里的指引部署环境，安装工具，链接GitHub，完成初始化，才是后续；[@Deep Research](plugin://deep-research-work@openai-curated-remote) 看看有没有类似的agent友好项目的说明文档，然后再升级我们的readme和项目

## 客户端范围补充

Claude Code／WorkBuddy / Codex / Deepseek Harness / Kimi Code / Zcode / cursor / TraeWork / QcodeWork

## 实施授权与完整批准计划

以下为用户要求实施的完整计划。其末尾保留了方案形成时的只读计划阶段说明；本条新的 “PLEASE IMPLEMENT THIS PLAN” 已明确授权本地实施，并未授权推送、PR 或合并。

PLEASE IMPLEMENT THIS PLAN:

# SZTU Connect 多 Agent「一句话开始」升级计划

## 1. 目标与研究结论

将快速开始从“开发者手动配置环境”改为：

**用户选择自己熟悉的本地 Agent，发送一句话；Agent 按项目指引准备环境、安装适用工具、运行示例，再带用户创建第一条记录。**

覆盖 Claude Code、WorkBuddy、Codex、DeepSeek Harness、Kimi Code、ZCode、Cursor、TraeWork、QoderWork。用户只需拥有其中一种可正常工作的客户端，不要求安装全部客户端，也不要求先安装 SZTU Connect 专属插件。

保留已经确认的选择：

- **本地体验优先**：不把 GitHub 登录作为开始使用的前提。
- **首次配置附带工具**：安装当前操作系统适用的工具，而不是把它们全部推迟到以后。
- **Windows、macOS 为首版完整验收平台**；Linux 保留已有手动 CLI 路径。

研究中最值得采用的是三个做法：[Agent Reach](https://github.com/Panniantong/Agent-Reach/blob/da5044d26fc6adddb6554d5679c94ac22e76e428/docs/install.md)将面向人的一句话入口与面向 Agent 的安装指南分开；[Superpowers](https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/README.md#installation)明确区分不同客户端的接入方式；[gstack](https://github.com/garrytan/gstack/blob/0d1bd5616c0ef096bb7ccee336f63c60ee408618/README.md#install--30-seconds)把安装助手与第一次实际使用衔接起来。本项目借鉴这些结构，不复制其业务功能、自动更新或自动提交行为。

## 2. README：先让普通用户开始，再提供开发者命令

保留现有品牌文案、完整「构史」释义、古典段落及其顺序，集中调整快速开始和相关导航。

### 主入口

将现有快速开始的第一部分改为“交给 Agent 开始”，提供一条可以直接复制的消息：

```text
请阅读 https://raw.githubusercontent.com/Shuang-su/sztu-connect/main/docs/GETTING_STARTED.md ，按指引在本机安装并初始化 SZTU Connect，配置适用的附带工具、跑通示例，完成后带我记录第一件校园往事。
```

紧接提示词，用简短文字说明：

- **开始前**：打开支持本地文件和命令操作的 Agent，选择一个用于保存项目的文件夹。
- **Agent 会完成**：获取项目、检查并准备环境、配置工具、验证运行结果，告诉你记录保存在哪里。
- **你可能需要完成**：确认安装位置、处理系统授权或安装窗口；需要同步时，再登录 GitHub。

“一句话开始”不写成“全程零确认”。用户不需要自己编写安装命令，但账号登录和系统授权仍由用户完成。

### 后续阅读顺序

快速开始内部调整为：

1. 交给 Agent 初始化；
2. 查看初始化结果和示例；
3. 准备材料，创建第一条记录；
4. 需要时连接 GitHub，同步或贡献；
5. 开发者手动安装方式。

现有 Python、虚拟环境、安装和测试命令保留在开发者折叠区。九种客户端的详细差异放进上手指南，README 不堆九套安装教程。

## 3. 项目能力：一份指南，一个可重复运行的初始化助手

### 共用指引与入口

新增 `docs/GETTING_STARTED.md`，作为初始化流程的唯一详细说明，包含客户端选择、环境准备、工具安装、失败恢复、GitHub 接入和完成判定。

项目根 `AGENTS.md` 增加简短的初始化路由；Claude Code 使用薄的 `CLAUDE.md` 导入现有项目约定，不复制整份规则。现有 Codex 插件增加 `setup-sztu-connect` Skill 和初始化提示入口，技能只负责定位用户工作副本、读取共用指南并执行流程。

不让各客户端自己的 `/init` 重新生成或覆盖本项目的指令文件；不把插件缓存目录当作用户的档案仓库。

### 初始化助手

新增纯 Python 标准库实现的 `scripts/bootstrap.py`，在 Agent 准备好可用 Python 后运行，提供：

- `--root`：明确目标项目目录；
- `--check`：只检查，不安装、不改文件；
- `--json`：输出结构化阶段结果，便于不同 Agent 判断下一步。

初始化按以下顺序执行：

1. **识别实际环境。** 确认客户端、本机或隔离环境、操作系统、架构、目标目录及权限；已有正确工作副本就复用，否则在选定目录建立独立副本。遇到目录冲突先停下，不覆盖现有项目。
2. **准备基础环境。** 复用满足要求的 Python 和 Git；缺失时由 Agent 按官方安装方式引导。项目依赖安装到独立虚拟环境，使用现有依赖锁文件，不要求用户手动激活虚拟环境，也不改全局 Python 包。
3. **配置适用的附带工具。** 对接“添加可信来源工具存档”任务交付的固定版本、平台、来源与校验清单；按当前平台获取所需文件，确认 Git LFS 实体和 SHA-256，再进入正常安装流程。安装成功不能仅凭安装包存在判断。
4. **跑通首次体验。** 在忽略目录中准备隔离的最小示例，调用现有校验、构建、知识导出及聊天示例能力，展示实际结果。示例不写入正式校园记录。
5. **交付可继续使用的状态。** 分别报告基础环境、附带工具、示例和 GitHub 状态，给出项目位置、查看结果的入口，以及创建第一条记录的提示。

重复运行时重新核对实际状态，只补未完成部分；中断后可以通过“继续初始化”恢复，不重复克隆、不清空环境、不覆盖用户内容。阶段结果区分完成、待用户操作、失败和不适用，不能把部分成功包装成全部完成。

初始化日志和状态保存在 `.work/`，下载缓存遵循项目现有目录约定，并复用输出路径边界检查。初始化只准备工具，**不自动读取聊天历史、启动 Computer History 采集或导入用户原件**。

### GitHub 按需接入

用户要求同步或贡献时，再检查 GitHub CLI 和现有授权，使用浏览器登录流程；不要求用户把 Token 发到聊天里。登录后核对目标仓库权限：有写权限就使用工作分支，没有则复用或创建 Fork。保留已有远端配置，不盲目覆盖 `origin`、`upstream`。[GitHub 登录文档](https://cli.github.com/manual/gh_auth_login)、[Fork 文档](https://cli.github.com/manual/gh_repo_fork)

初始化本身不自动 push、创建 PR 或合并。没有登录 GitHub 不影响本地初始化成功。

## 4. 九种客户端的适配边界

所有客户端都保留“显式读取同一份指南”的通用入口；原生规则、Skill 或插件仅用于改善发现和后续使用，不作为统一安装格式。

| 客户端 | 本轮采用的接入方式与必要说明 |
|---|---|
| **Claude Code** | 在本地项目执行，通过 `CLAUDE.md` 导入 `AGENTS.md`。不能假定它会直接自动读取 `AGENTS.md`。[官方说明](https://code.claude.com/docs/en/memory) |
| **WorkBuddy** | 选择本地工作空间，使用可执行任务的 Craft 模式，或确认计划后执行；显式读取指南，原生 Skill 导入作为便捷入口。[官方任务说明](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Task-Bar) |
| **Codex** | 使用本地项目、根 `AGENTS.md` 和现有插件的初始化 Skill；没有安装插件时仍可使用通用提示词。[项目指令](https://learn.chatgpt.com/docs/agent-configuration/agents-md)、[插件说明](https://learn.chatgpt.com/docs/plugins) |
| **DeepSeek Harness** | 使用官方 `dsh` 的本地工作区及可用文件、命令工具；复用项目指令，但不依赖 `@path` 导入。因产品仍是 Developer Preview，标为实验入口。[官方介绍](https://www.deepseek.com/harness/en/)、[指令加载说明](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/context/agent-instructions/README.md) |
| **Kimi Code** | 使用本地 CLI 会话，显式读取指南；可以复用标准 Skill。不要用客户端 `/init` 覆盖已有项目规则。[快速上手](https://www.kimi.ai/zh-hans/help/kimi-code/cli-getting-started)、[Skill 文档](https://moonshotai.github.io/kimi-code/en/customization/skills) |
| **ZCode** | 先选择项目工作区；利用当前工作区根 `AGENTS.md`，不假定递归加载或 `@import`。无项目会话不能直接转为项目会话时，明确引导新建项目任务并继续。[官方说明](https://zcode.z.ai/en/docs/agents) |
| **Cursor** | 使用本地项目中的 Agent，复用根 `AGENTS.md`；不把仅问答或云端 Agent 当作本机安装入口。[规则文档](https://cursor.com/docs/rules)、[Agent 文档](https://cursor.com/docs/agent/overview) |
| **TraeWork** | 使用桌面本地任务；Windows 初始化宿主机环境时选择 **Code 模式**，因为 Work／Design 使用隔离虚拟环境。后续自动加载 `AGENTS.md` 需启用官方导入开关。[沙箱说明](https://docs.trae.cn/work_sandbox)、[规则说明](https://docs.trae.cn/work_rules) |
| **QoderWork** | 使用用户授权的 Working Folder，显式读取指南或通过官方支持的 GitHub Skill 链接安装方式进入；先验证实际命令环境，不假定具有与 Qoder CLI 相同的规则发现机制。[Skill 文档](https://docs.qoder.com/qoderwork/skills)、[文件管理](https://docs.qoder.com/qoderwork/file-management) |

本轮不独立发布九套应用市场插件，也不为未知机制编造配置文件。需要切换工作区、刷新 Skill 或重新开任务时，指南明确提供接续步骤。

## 5. 验收、交付与默认边界

### 自动化验证

- 覆盖全新初始化、重复运行、中断恢复、已有有效环境、缺失或不兼容 Python、含中文及空格的路径。
- 覆盖目录冲突、虚拟环境或输出路径越界、安装失败、网络失败、LFS 指针未下载、文件哈希不匹配。
- 覆盖 GitHub 未登录仍可本地使用、有写权限走分支、无权限走 Fork、已有远端不被覆盖。
- 首次使用验证不依赖“正式 Event 数量必须为零”；现有空骨架断言调整为专门的测试夹具约束，避免用户添加真实记录后被误判失败。
- 保留现有单元测试、数据校验和构建一致性检查；新增 Windows、macOS 初始化测试，现有 Linux 检查继续保留。

### 实际体验验证

九种客户端均建立带版本、系统和执行模式的验收记录，检查是否真正完成：读取指南、准备环境、配置适用工具、展示示例、重新打开项目后继续使用。未实测的组合明确标为“待验证”，不能因为文档格式兼容就标成完整支持。

README 同时检查 GitHub 渲染、导航、相对链接和复制提示词。公开提示词中的指南 URL 在文档进入默认分支后再验证；本地阶段不得把尚未发布的链接报告为可用。

### 交付边界

- 在独立 `codex/agent-first-onboarding` 分支实施，按项目约定保存研究依据、最终计划、验证结果和完成记录，形成可审查的本地 checkpoint。
- 附带工具完整验收依赖另一任务的归档清单与文件交付；缺少这部分时明确报告依赖，不自行更换工具或宣称安装完成。
- 不改变现有数据模型、导出格式和内容校验策略，不改写用户已有品牌文案，不新增网站、RAG 服务或自动发布功能。
- 本次截至 **2026-09-03** 完成的是第一方文档调研与静态核对；尚未执行九种客户端的真实安装。本轮处于计划模式，未修改文件、安装软件、登录账号或更改 GitHub 状态；后续实施默认也不 push、开 PR 或合并，除非获得新的明确要求。
