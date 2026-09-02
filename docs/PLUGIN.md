# Agent plugin

## v0.1 实际能力

仓库根是 `sztu-connect` Codex plugin：

- `.codex-plugin/plugin.json`：展示与发现信息
- `skills/`：instruction-only 工作流
- `src/sztu_connect/`：本地确定性 CLI

Plugin manifest 不声明 `mcpServers`、`apps` 或 hooks。仓库也没有 MCP/WebMCP runtime；文档中的相关字样只用于明确“不存在该能力”，不能作为接口承诺。

## 使用方式

作为 plugin 安装时，Codex 从根 `skills/` 发现工作流；直接打开仓库时，根 `AGENTS.md` 也会把 Agent 引导到同一目录，因此不维护第二份 skill 镜像。

Plugin 安装只让 Skill 可被发现，不会自动安装 Python 包，也不把插件缓存目录当作用户史料库。创建或修改记录前，先选择一个用户拥有的 SZTU Connect clone，并在该 clone 按 `README.md` 创建本地虚拟环境、安装 `requirements.lock` 与项目 CLI。若 CLI 不可用，Skill 必须先完成这一步或明确报告缺少运行环境，不能跳过校验，也不能把正式 Event 写进插件安装缓存。

Skill 可以让 Agent 创建或修改文件，但不会替代用户对 push、PR、发布、网页抓取或远程向量库写入的授权。CLI 不联网，也不会执行投稿内容。

## 验证

```bash
python3 /path/to/plugin-creator/scripts/validate_plugin.py .
python3 /path/to/skill-creator/scripts/quick_validate.py skills/<skill-name>
```

插件校验只证明 manifest 和目录结构可被识别；行为仍由单元测试、端到端构建与独立 Agent 演练验证。
