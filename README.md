# 🐔🧱时空

`SZTU Connect` 是项目在纯文本、包名、命令行和协议字段中的名称；面向屏幕阅读器及其他无障碍场景时使用“技大时空”。

这是一个以事件为核心、以时间为坐标、以来源为依据的深圳技术大学非官方历史记录仓库。它首先是一套可复制的数据结构和本地工具：任何人都可以在自己的 clone 或 fork 中提交一个事件，再由 Agent 关联相关人物、组织、地点、制度、主题与其他事件，不依赖中心化服务，也不预设治理角色。

## 当前可用

- 事件真源：`content/events/<年份或 undated>/<event-id>/event.json`
- 目录节点：人物、组织、地点、制度与主题只保存稳定 ID、别名和必要说明
- 来源级和论断级引用：每个事实可定位到具体来源及页码、段落或时间码
- 双向链接：事件只写一份正向关系，构建器像 Notion／Obsidian 一样生成反向链接和各目录索引
- 多种史体：同一批事实记录可组织为编年体、纪传体、典制体、纪事本末体或其他专题集合
- Agent/plugin：仓库本身是一个 Codex plugin，能力由 `skills/` 与本地 CLI 提供
- 向量知识库出口：确定性生成、供应商无关的 JSONL；embedding 默认留在本地，不进入 Git
- 分级隐私检查：秘密和高风险直接标识会阻断；普通联系方式等只提示核查，不要求默认脱敏

当前没有实现 MCP Server、WebMCP、网站、云端向量库或自动发布。插件不会声明这些不存在的能力。

## 数据流

```text
Source ── supports / contradicts / context ──> Claim
Claim  ── belongs to ──> Event
Event  ── links to ──> Person / Organization / Place / Institution / Topic / Event
Collection ── arranges ──> Events
                            │
                            ├─ timeline.json
                            ├─ backlinks.json
                            ├─ directories/*.json
                            ├─ graph.json
                            └─ knowledge/chunks.jsonl
```

Event、Source、Node、Collection 的 JSON/Markdown 是唯一真源；所有目录和索引都可以在任意 clone 中重建。Markdown 可使用 `[[target-id|显示文字]]` 导航，构建器会校验目标并生成 backlink；带证据的关系仍写在 Event JSON 中。

## 多种史体

史体是对同一批 Event 的组织方式，不复制或改写事件事实：

| `form` | 形式 | 用法 |
|---|---|---|
| `annals` | 编年体 | 按时间排列一组记录 |
| `biographical` | 纪传体 | 围绕人物、组织或其他主体串联记录 |
| `institutional` | 典制体 | 记录制度、机构、空间或规则的沿革 |
| `thematic` | 纪事本末体／专题 | 围绕一件事或一个主题组织始末 |

每个集合只保存稳定 `event_id`；实际时间顺序由构建器从事件中生成。

## 快速开始

需要 Python 3.11 或更高版本。

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.lock
python -m pip install --no-deps -e .

sztu-connect doctor
sztu-connect check --json
python -m unittest discover -s tests
```

让 Agent 开始第一条记录时，可以直接说：

```text
使用 record-campus-event skill，根据我提供的来源创建一个事件。
自动查找或建立相关人物、组织、地点、制度与主题节点，并生成双向链接索引。
保留可核查的姓名、日期和上下文；不要猜测未知信息。
完成后运行 sztu-connect check --json。
```

结构示例位于 `examples/minimal/`。示例不进入正式索引。

## 事实与隐私

- 原样记录有来源支持、与校史相关的姓名、公开职务、日期和上下文，不因“出现个人信息”自动匿名化。
- `fact` 和 `allegation` 必须带支持来源；反证使用 `role: contradicts` 并与原论断并列保存。
- 不确定的时间、身份和因果关系保持不确定，不由 Agent 补齐。
- 密码、Token、Cookie、私钥、完整证件号、可用于身份接管的信息、私人精确住址和实时位置不得进入公开记录或向量索引。
- 电话、邮箱、学号样式、聊天昵称等默认产生 `review` 提示；提示本身不让检查失败，记录者依据事实核查必要性选择原样、最小化或限制索引。
- 脱敏不修改原始材料；公开派生副本与来源哈希继续保持关联。

详见 `docs/FACT_CHECKING.md` 与 `docs/PRIVACY.md`。

## 目录

```text
.codex-plugin/       Codex plugin manifest
skills/              Plugin 可发现的 Agent 工作流
content/events/      事件真源
content/nodes/       人物、组织、地点、制度与主题节点
content/collections/ 多种史体与专题组织
sources/records/     来源元数据
schemas/             JSON Schema
src/                 确定性 CLI 与构建器
data/generated/      可重建时间线、链接图和知识 JSONL
examples/minimal/    不进入正式索引的结构示例
.work/               本地私有输出；不提交
```

## 命名

- 中文显示名称：🐔🧱时空
- 纯文本名称：SZTU Connect
- 无障碍名称：技大时空

## 许可

代码、原创叙事、结构化元数据和第三方来源采用分层许可，见 `LICENSE.md`。第三方材料的权利状态始终由各自来源记录说明。
