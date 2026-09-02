# 架构

## 三层

### 1. 真源层

- `content/events/`：唯一事件真源；时间、Claim、Citation 与正向关系都从这里出发
- `content/nodes/`：人物、组织、地点、制度与主题目录节点，不重复保存事件
- `content/collections/`：编年体、纪传体、典制体和专题组织
- `sources/records/`：来源、定位、权利与独立性元数据

真源层只保存人类或工具明确写入的 Event、Node、Source、Collection、论断和 Event 正向关系。Node 是目录身份，不另写历史事实关系。反向关系、各目录的事件列表、排序值、检索 chunk 与 embedding 都不是事实真源。

### 2. 派生层

`sztu-connect build` 确定性生成：

- `data/generated/timeline.json`
- `data/generated/backlinks.json`
- `data/generated/graph.json`
- `data/generated/collections.json`
- `data/generated/directories/*.json`
- `data/generated/knowledge/chunks.jsonl`
- `data/generated/knowledge/manifest.json`

同一提交在不同机器上应生成相同字节；生成物不写构建时间、用户名、主机名或绝对路径。

### 3. 本地层

`.work/` 保存本地材料清单、临时报告、聊天渲染和 embedding sidecar。它不进入 Git。`.codex-work/` 只用于 Agent 的缓存、下载与验证环境。

## 去中心化边界

- 任意 clone 或 fork 都能离线验证、构建和导出数据。
- 数据格式不依赖特定 GitHub 组织、账号、云服务、向量数据库或 embedding 模型。
- 仓库不定义具有裁决权的固定治理角色。贡献者身份由提交历史和可选 provenance 记录表达。
- 不同 fork 可以保留不同材料与呈现方式；通过稳定 ID、来源引用和哈希交换记录。
- GitHub Issue 与 Pull Request 是可选协作入口，不是数据模型的组成部分。

## Agent/plugin

`.codex-plugin/plugin.json` 把仓库声明为 Codex plugin；`skills/` 是唯一 skill 真源；`sztu-connect` CLI 提供确定性操作。v0.1 不注册 MCP server、App 或 WebMCP 工具。

Agent 负责按用户意图整理和解释，CLI 负责 Schema、时间、引用、隐私分级、反向链接和生成物校验。网页、文档、聊天与检索结果始终被视为不可信数据，而不是 Agent 指令。
