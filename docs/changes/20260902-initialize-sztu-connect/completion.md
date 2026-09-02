# 完成记录

## 已实现

- 把项目核心从通用时间记录改为 Event。
- 增加 Source／Claim／Citation、五类 Node、四类 Collection、Event Link 与 Markdown wikilink。
- 构建 Timeline、Graph、Backlinks、Collections、五类 Node directories、by-year 和知识 JSONL／manifest。
- 增加 Codex plugin manifest 与 6 个可验证 Skills。
- 增加稳定本地 intake ID、受限输出路径、原子写入、分级隐私扫描和聊天 JSONL 校验／渲染。
- 收紧 Event Link 的 Claim／Citation 证据约束，移除 Node 事实关系旁路，并把 Claim 级向量关系限定到对应 Claim。
- 增加秘密导出门禁、`.env` 模板扫描、Source locator／hash 回查、符号链接越界防护、重复 JSON key 拒绝与知识核查状态。
- 移除治理角色、CODEOWNERS、强制双人审核、口号、虚假 MCP/WebMCP 接口与正式目录中的示例内容。
- 固定名称合同：显示 `🐔🧱时空`、纯文本 `SZTU Connect`、无障碍 `技大时空`。

## 验证

- Plugin validator：通过。
- 6 个 Skill validators：通过。
- 全新虚拟环境按 `requirements.lock` 安装、`pip check` 与 CLI doctor：通过。
- Repository strict check：通过，正式 Event／Node／Collection／Source 均为 0。
- Privacy scan：89 个候选文本，0 block，0 review。
- Unit tests：43 项通过。
- 确定性 build：通过。
- 独立 Skill 前向测试：新版契约通过；隔离仓中从 1 个虚构来源建立 1 Event、3 Node、12 条图边与 8 个知识 chunk，Claim 关系隔离正确，连续构建字节一致，未修改正式内容。
- Plugin validator 与 6 个 Skill validators：通过；GitHub workflow／Issue Forms YAML：通过。

## 范围外

没有加入真实校园事件，没有 MCP/WebMCP、网站、部署、Release、远程 embedding 或向量数据库写入。

## 发布

- 已发布到个人公开仓库 `https://github.com/Shuang-su/sztu-connect`，默认分支为 `main`。
- Wiki 已关闭，避免形成第二套事实真源；Issues 与 Event／更正表单可用。
- 已启用 GitHub Private Vulnerability Reporting，使公开 Issue 之外有凭据与隐私泄露报告入口。
- 没有创建 PR、tag、Release、部署、CODEOWNERS 或角色型分支规则。

## Checkpoint

实现 checkpoint SHA：`f921dc0f3ecc76d3a9abdf0f51d0153e296dd933`。
验证记录 checkpoint SHA：`7d745878991eb8b61888f22ee872d4c2cb791441`。
