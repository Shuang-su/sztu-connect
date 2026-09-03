# Agent plugin

## v0.1 实际能力

仓库根是 `sztu-connect` Codex plugin：

- `.codex-plugin/plugin.json`：展示与发现信息
- `skills/`：instruction-only 工作流
- `src/sztu_connect/`：本地确定性 CLI
- `scripts/bootstrap.py`：项目内环境准备与初始化检查助手

Plugin manifest 不声明 `mcpServers`、`apps` 或 hooks。仓库也没有 MCP/WebMCP runtime；文档中的相关字样只用于明确“不存在该能力”，不能作为接口承诺。初始化 Skill 不依赖新增的运行时接口。

## 使用方式

作为 plugin 安装时，Codex 从根 `skills/` 发现工作流；直接打开仓库时，根 `AGENTS.md` 也会把 Agent 引导到同一目录，因此不维护第二份 skill 镜像。

Plugin 安装只让 Skill 可被发现，不会自动安装 Python 包，也不把插件缓存目录当作用户史料库。创建或修改记录前，选择用户拥有的 SZTU Connect 工作副本。可以调用 `setup-sztu-connect`，由 Agent 按 [共用上手指南](GETTING_STARTED.md) 准备环境、适用工具和示例；未安装插件的客户端也可显式读取该指南开始。

初始化过程中，助手把依赖装进该工作副本的 `.venv/`，Agent 负责系统安装与授权交接。已有 CLI 可用时直接复用；依赖缺失或工具尚未就绪时明确报告阶段状态，不能跳过校验或把正式 Event 写进插件缓存。安装包存在不等于应用安装成功，文档适配也不等于该客户端已通过完整体验验收。

根 `skills/` 保持单一来源。Claude Code 通过薄的 `CLAUDE.md` 导入项目规则；其他客户端按各自已证实的规则 / Skill 机制接入，或显式读指南，不共用 Codex manifest 作为九种客户端的统一安装格式。

Skill 可以让 Agent 创建或修改文件，但不会替代用户对 push、PR、发布、网页抓取或远程向量库写入的授权。内容 CLI 不联网，也不会执行投稿内容；初始化助手的安装模式会按锁文件安装依赖、按工具清单下载固定文件。`--check` 不安装、不下载、不构建、不写状态，GitHub 查询另需显式 `--github`。

## 验证

```bash
python3 /path/to/plugin-creator/scripts/validate_plugin.py .
python3 /path/to/skill-creator/scripts/quick_validate.py skills/<skill-name>
```

插件校验只证明 manifest 和目录结构可被识别；行为仍由单元测试、端到端构建与独立 Agent 演练验证。
