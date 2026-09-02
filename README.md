# SZTU Connect

## 🐔🧱构史 · G.O.U.S.H.I.
**以事实为基，以时间为轴，
以众声为脉，以链接构史。<br>
拾校园之片羽，构时代之长卷。**

### 为什么叫「构史」

故事，是人们记得的过去；<br>
历史，是过去留下的痕迹；<br>
构史，将散落在人群、文件、影像与网络中的片段重新连接，使它们重新构筑来源、时间、关系与上下文。

我们记录事件，保存来源，连接人物与地点，容纳不同视角。

一件事可以进入年表；<br>
一个人可以由许多事件留下轨迹；<br>
一种制度可以观察其沿革；<br>
一个主题也可以从无数片段中呈现始末。

当一块块散落的故事最终彼此连接——

**「构史」，便把故事构成历史。**

###Grounded Origins University Stories, History & Interlinks
**G — Grounded**
有据可依。
*每一段记录皆有所本，让事实落地。**

**O — Origins**
溯源。
*保存出处、时间、版本与传播脉络，让一则说法不仅“有据”，亦能知其所自。*

**U — University**
立足校园。
*记录校园中的人、事、物、地、制、时代与其彼此关系。*

**S — Stories**
故事。
*保存宏大叙事之外，每一个值得被记住的瞬间。*

**H — History**
历史。
*让散落的故事进入时间，成为可以追溯的历史。*

**I — Interlinks**
互链。
*让人物、组织、地点、制度、主题与事件彼此连接，构成校园记忆网络。*



##SZTU Connect · 技大时空**是一个以事件为核心、以时间为坐标、以来源为依据的深圳技术大学历史记录项目。

[快速开始](#快速开始) · [数据模型](docs/DATA_MODEL.md) · [参与贡献](CONTRIBUTING.md) · [长期目标](#长期目标)



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

## 数据如何组织

### 数据流

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

### 多种史体

史体是对同一批 Event 的组织方式，不复制或改写事件事实：

| `form` | 形式 | 用法 |
|---|---|---|
| `annals` | 编年体 | 按时间排列一组记录 |
| `biographical` | 纪传体 | 围绕人物、组织或其他主体串联记录 |
| `institutional` | 典制体 | 记录制度、机构、空间或规则的沿革 |
| `thematic` | 纪事本末体／专题 | 围绕一件事或一个主题组织始末 |

每个集合只保存稳定 `event_id`；实际时间顺序由构建器从事件中生成。

## 事实、来源与隐私

- 原样记录有来源支持、与校史相关的姓名、公开职务、日期和上下文，不因“出现个人信息”自动匿名化。
- `fact` 和 `allegation` 必须带支持来源；反证使用 `role: contradicts` 并与原论断并列保存。
- 不确定的时间、身份和因果关系保持不确定，不由 Agent 补齐。
- 密码、Token、Cookie、私钥、完整证件号、可用于身份接管的信息、私人精确住址和实时位置不得进入公开记录或向量索引。
- 电话、邮箱、学号样式、聊天昵称等默认产生 `review` 提示；提示本身不让检查失败，记录者依据事实核查必要性选择原样、最小化或限制索引。
- 脱敏不修改原始材料；公开派生副本与来源哈希继续保持关联。

详见 [事实核查](docs/FACT_CHECKING.md) 与 [隐私边界](docs/PRIVACY.md)。

## 长期目标

当前版本首先解决“过去发生了什么”：以 Event 为具有发生时间的历史事实原子，以 Source 支撑 Claim，并由 Node 与 Collection 建立可重建的目录、时间线和反向链接。

| 领域 | 主要回答的问题 |
|---|---|
| 校园历史 | 过去发生了什么 |
| 校园档案 | 有什么材料可以核验 |
| 校园信息 | 某个时间点什么信息有效 |
| 校园知识 | 某个概念如何理解、某件事如何办理 |

长期目标是在不改变 Event 历史语义的前提下，逐步建设社区可治理、Agent 可协作、证据优先、时间感知、本地可重建的校园知识基础设施。系统应保留来源、版本、矛盾与不确定性，并在证据不足、信息过期或问题前提错误时拒绝给出虚假的确定答案。

这是一项长期路线，不代表 Knowledge Record、全文检索、混合检索、RAG、网站或持续监测已经实现。路线拆分与完成条件见 [长期路线 Issue #1](https://github.com/Shuang-su/sztu-connect/issues/1) 和 [项目路线](docs/ROADMAP.md)。

## 参与项目与获取帮助

- 根据 [贡献指南](CONTRIBUTING.md) 提交一条有来源的校园事件，或补充、反驳和更正既有论断。
- 在 [GitHub Issues](https://github.com/Shuang-su/sztu-connect/issues) 报告问题、讨论数据模型或认领边界明确的工程任务。
- 参与来源整理、事实核查、Schema 与构建工具、数据质量、检索评测、安全隐私、文档或只读浏览体验。

贡献不要求一次实现完整系统。缺失信息可以保持未知，存在冲突的来源应并列保留；每项修改都应能够由公开来源、测试或可重建结果验证。

## 项目结构

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

## 致谢

SZTU Connect 在校园知识共享、个人记录保存、社区协作和网页归档方面受到以下开源项目的启发。这里的列举不表示本项目使用、捆绑或依赖其代码；各项目仍适用各自的许可证和使用边界。

- 本校信息整理：[SZTU-Information](https://github.com/Luv-Ray/SZTU-Information)。
- 校园知识共享与社区协作：[zju-icicles](https://github.com/QSCTech/zju-icicles)、[SUSTechapplication](https://github.com/SUSTech-Application/SUSTechapplication)、[SJTU-Application](https://github.com/SurviveSJTU/SJTU-Application) 和 [SurviveSJTUManual](https://github.com/SurviveSJTU/SurviveSJTUManual)。
- 个人记录保存与叙事：[WeChatMsg](https://github.com/LC044/WeChatMsg)、[wechatDataBackup](https://github.com/git-jiadong/wechatDataBackup) 和 [WeChat-Annual-Report-Generation](https://github.com/Jintian-JTST/WeChat-Annual-Report-Generation)。
- 网页归档：[Browsertrix](https://github.com/webrecorder/browsertrix)。

## 许可

代码、原创叙事、结构化元数据和第三方来源采用分层许可，见 [LICENSE.md](LICENSE.md)。第三方材料的权利状态始终由各自来源记录说明。

---

> 构众说以成卷，系众事而为史。
>
> 采校园片羽，系人物行迹，<br>
> 存制度沿革，录事件始末。
>
> 使散见之闻不止于谈资，<br>
> 使一时之事得归于时间。
>
> 其为「构史」，
>
> 既构其形，亦求其证。
>
> 有据构实，众声成史。
