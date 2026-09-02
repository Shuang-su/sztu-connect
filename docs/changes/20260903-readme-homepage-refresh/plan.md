# SZTU Connect README 与 GitHub About 更新计划

## 目标

把根 README 改造成正式、友好、可核查的项目首页，同时统一项目的活动名称合同：标准及公开名称使用 `SZTU Connect`，中文叙述使用“技大时空”，README 首页专属附属标题为 `🐔🧱构史 · G.O.U.S.H.I.`。

不新增 About Markdown 或 Manifesto，不改变数据模型、CLI、Schema、稳定 ID、知识 JSONL 或正式内容。

## README

1. 首页使用唯一一级标题 `SZTU Connect` 和二级附属标题 `🐔🧱构史 · G.O.U.S.H.I.`。
2. 英文全称只出现一次：`Grounded Origins University Stories, History & Interlinks`。
3. 首屏依次展示“以事实为基，以时间为轴，以众声为脉，以链接构史。”“拾校园之片羽，构时代之长卷。”和自然嵌入“技大时空”的项目简介。
4. 完整解释：
   - `G — Grounded`：有据可依，每一段记录皆有所本。
   - `O — Origins`：保存出处、时间、版本与传播脉络。
   - `U — University`：记录校园中的人、事、物、地、制、时代与关系。
   - `S — Stories`：保存宏大叙事之外值得记住的瞬间。
   - `H — History`：让故事进入时间并可以追溯。
   - `I — Interlinks`：连接人物、组织、地点、制度、主题与事件。
5. “为什么叫「构史」”保留用户最终文本，说明事件进入年表、人物留下轨迹、制度呈现沿革、主题呈现始末，并以“「构史」，便把故事构成历史。”收束。
6. 主体顺序为：当前可用、快速开始、数据如何组织、事实来源与隐私、长期目标、参与与帮助、项目结构、致谢、许可、无标题古典收束段。
7. 删除旧名称说明和 `## 命名`，保留当前能力边界、快速开始、数据流、史体表格、隐私规则和目录说明。
8. 长期目标概括校园历史、档案、信息和知识四个领域，并链接公开 Issue #1；明确长期能力尚未实现。
9. 致谢按本校信息、校园知识共享、个人记录保存和网页归档分组，列出 SZTU-Information、zju-icicles、SUSTechapplication、SurviveSJTU 两个项目、WeChatMsg、wechatDataBackup、WeChat-Annual-Report-Generation 与 Browsertrix；说明这些是启发而非依赖。
10. README 最后以 blockquote 保留完整古典段落，最后一句为“有据构实，众声成史。”，其后不再添加内容。

## 名称合同与运行时

- `connect.config.json` 的 `display_name` 与 `plain_text_name` 均为 `SZTU Connect`，`accessible_name` 保持“技大时空”。
- 插件 `displayName` 改为 `SZTU Connect`，长描述自然写入 `SZTU Connect（技大时空）`，不使用 README 附属标题。
- 聊天重建页显示 `SZTU Connect／技大时空`，不再显示旧 emoji 名称。
- 根 Agent 约定改为公开标识规则，并限制附属标题只作为 README 首页品牌文案。
- 更新单元测试，覆盖配置、插件、聊天页、README 标题、英文全称单次出现、`H — History` 和末尾收束。
- 不修改历史变更记录中的旧名称合同。

## 路线与 GitHub About

- `docs/ROADMAP.md` 增加长期路线摘要并链接 `https://github.com/Shuang-su/sztu-connect/issues/1`，不复制整份 Epic。
- 待 README 发布到默认分支时，将 GitHub About Description 设置为：`构众说以成卷，系众事而为史。SZTU Connect（技大时空）：以事件为核心、以时间为坐标、以来源为依据的深圳技术大学非官方校园历史记录项目。`
- Website 保持为空。
- Topics 使用：`bidirectional-links`、`campus-archive`、`campus-history`、`codex-plugin`、`digital-archive`、`digital-history`、`fact-checking`、`knowledge-graph`、`local-first`、`provenance`、`sztu`。
- 不添加 `rag`、`mcp-server`、`webmcp`、`website` 或 `vector-database`。
- Release、Deployment、Package 为空时不在仓库首页展示。

## 验证与发布

1. 校验两个 JSON 文件可解析，README 标题、名称、字母顺序、末尾内容和链接正确。
2. 运行 doctor、validate、privacy-scan、两次 build、check 和全部单元测试；两次构建必须一致，隐私扫描不得有 `block`。
3. 运行 `git diff --check`，确认没有无关文件或事实数据变化。
4. 在 `codex/readme-homepage-refresh` 上创建原子 checkpoint commit。
5. 未收到明确发布指令时不 push、不创建 PR、不合并、不修改远端 About；发布时让 README 与 About 同步生效并复核公开首页。
