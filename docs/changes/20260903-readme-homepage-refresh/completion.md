# 完成记录

## 已实现

- README 以 `SZTU Connect` 为唯一一级标题，以 `🐔🧱构史 · G.O.U.S.H.I.` 为首页附属标题，并自然使用中文名称“技大时空”。
- 加入 `Grounded Origins University Stories, History & Interlinks`、G／O／U／S／H／I 六项释义和最终版“为什么叫「构史」”。
- 重排当前能力、快速开始、数据组织、事实与隐私、长期目标、参与入口、项目结构、致谢和许可；完整古典段落作为 README 最后内容。
- 长期目标概括校园历史、档案、信息和知识四个领域，并链接公开 Issue #1；未把 Knowledge Record、RAG、网站、MCP、WebMCP 或持续监测表述为已实现能力。
- 致谢按本校信息、校园知识共享、个人记录保存和网页归档分组，并明确这些项目是启发而非代码依赖。
- `docs/ROADMAP.md` 增加长期路线入口，以 Issue #1 作为详细阶段与验收条件的权威页面。
- 活动名称合同已统一：配置与插件显示名使用 `SZTU Connect`，中文名称保持“技大时空”，聊天重建页自然显示两者；旧 emoji 名称只保留在历史变更记录中。
- 新增 README 与插件名称合同测试；没有改变 CLI、Schema、稳定 ID、正式内容或知识 JSONL 格式。

## 验证

- JSON 解析：`connect.config.json` 与 `.codex-plugin/plugin.json` 通过。
- CLI doctor：通过；Python 3.13.5，本地 CLI 与 Skills runtime 可用。
- Schema 与跨记录校验：通过；Event、Node、Collection、Source 当前均为 0。
- 隐私扫描：92 个文件，0 block、0 review、0 notice。
- 确定性构建：连续两次通过，聚合摘要均为 `ff31e3890c52c06824901b5404d8177f9aa731983e692255ab6d14b92103c6ca`。
- Repository check：通过。
- 单元测试：44 项通过。
- `git diff --check`：通过。
- GitHub Markdown API 渲染：一级标题、附属标题、英文全称和引用块正常。
- 本地相对链接、9 个致谢仓库链接与公开 Issue #1：均已验证；Issue #1 仍为 OPEN。
- About 待用 Description 为 72 个字符，处于 GitHub 简短描述容量以内。

## GitHub About 待发布设置

- Description：`构众说以成卷，系众事而为史。SZTU Connect（技大时空）：以事件为核心、以时间为坐标、以来源为依据的深圳技术大学非官方校园历史记录项目。`
- Website：保持为空。
- Topics：`bidirectional-links`、`campus-archive`、`campus-history`、`codex-plugin`、`digital-archive`、`digital-history`、`fact-checking`、`knowledge-graph`、`local-first`、`provenance`、`sztu`。
- 首页模块：Releases、Deployments、Packages 在为空时不显示。

## 发布状态与已知边界

- 本次按计划只完成本地实现与 checkpoint，没有 push、PR、merge、tag、Release 或部署。
- 远端 GitHub About 尚未修改，避免它先于默认分支 README 生效。
- 默认分支公开首页仍是旧 README；需要用户另行明确要求发布后，才能同步推送 README 并更新 About，再进行公开页面验收。
- 为运行测试创建了被 `.gitignore` 忽略的本地 `.venv`；pip 缓存位于 `.codex-work/cache/pip`，均未纳入提交。

## Checkpoint

- 名称合同与运行时：`14aba42`（`chore(branding): align public project names`）。
- README、路线图、请求与计划：`f05b0ac`（`docs(readme): refresh project homepage`）。
