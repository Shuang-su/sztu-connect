# 完成记录

## 结果

- 以远端 `main` 的 `903bdd51b3391dd6e85399c5bfdae6b2bb5922d6` 为基线，在 `codex/readme-archive-onboarding` 完成本地实施。
- 核心介绍明确为面向深圳技术大学的非官方数字档案计划，说明 Codex Plugin、本地工具与记录者的协作，以及尚未实现的检索与 RAG 目标。
- 新增三个记录场景、材料准备、本地环境说明、Agent 提示后的核对与结果入口；最小结构示例继续明确为非真实校园史料。
- 保留数据关系图和史体表格，把目录树移入折叠区；区分资料贡献、工具开发和求助入口。
- 长期目标补充当前、下一步和长期三个阶段；保留四领域表及公开 Issue #1，不增加跨学校承诺。
- 逐段比较确认：核心介绍前的字母释义与古典文案，以及从致谢开始的许可与收束段，均与用户最新远端版本完全一致。

## 新增材料说明

- 聊天记录：将“仓库工具导出聊天记录”精确化为处理用户已经合法取得的聊天导出。现有能力是 Agent 按 Schema 映射字段、`validate-chat` 校验 JSONL、`render-chat` 重建通用 HTML；未新增平台导出器、自动格式转换或解密能力。
- 图片与视频：补充细节文字、高清原图、EXIF、视频及其上下文的佐证价值，也说明材料不完整、元数据可变和私人位置等公开风险。原件与公开副本分开，不能将扫描通过等同于图像或视频已经过人工审查；未新增元数据读取、核验或清除工具。
- Computer History：按用户追加请求及已安装 Computer History 技能说明，加入用户单独启用、授权后查找相关活动片段的可选入口。要求回到原网页、文档或消息核验，区分电脑操作时间与校园事件时间；不捆绑、不自动启用、不新增活动流导入或后台监测。
- 本轮没有查询 Computer History 状态或实际活动，没有调整观察设置，也没有读取真实聊天、图片、视频或其他私人原件。

核对依据包括现有 [插件说明](../../PLUGIN.md)、[聊天导出说明](../../CHAT_IMPORT.md)、[事实核查](../../FACT_CHECKING.md)、[隐私边界](../../PRIVACY.md) 和 Computer History 技能说明。元数据可以被工具读写的说明另核对了 [ExifTool 官方仓库](https://github.com/exiftool/exiftool)，未引入该工具作为依赖。

## 测试调整

- 实施前复现 44 项测试中的唯一失败：旧 README 测试要求精确的文本前缀，无法容纳用户已经保存的排版。
- 将 README 检查拆入 `tests/test_readme.py`，保留项目名称、唯一一级标题、首页附属标题、唯一英文展开、G/O/U/S/H/I 六项顺序与单数 History 的约束。
- 正例覆盖强调方式、空行、前置说明及结尾变化；反例覆盖改名、额外一级标题、旧五字母版本、重复展开、复数 History、缺失字母及顺序变化。
- 代码块中的示例标题不参与公开名称判断；新增 README 相对链接存在性与仓库路径边界检查。
- 没有修改 CLI、插件配置、Schema、依赖、正式记录或生成数据。

## 验证结果

所有命令均使用项目已有 `.venv`；没有新增运行依赖。

| 检查 | 结果 |
|---|---|
| 配置及插件 manifest 的 JSON 解析 | 通过 |
| `sztu-connect doctor` | 通过；Python 3.13.5，本地 CLI 与 Skills runtime |
| `sztu-connect validate --json` | 通过；Event、Node、Collection、Source 均为 0，未创建真实记录 |
| `sztu-connect privacy-scan --json` | 通过；0 block、0 review、0 notice |
| 连续两次 `sztu-connect build --json` | 均通过；12 个生成文件的 SHA-256 清单一致 |
| `sztu-connect check --json` | 通过 |
| `python -m unittest discover -s tests` | 48 项通过 |
| `git diff --check` 与暂存区检查 | 通过 |
| `validate-chat` 与 `render-chat` | 仓库内 2 条结构示例消息通过校验并生成 HTML；`normalized: false` |

正式数据、Schema、源代码、插件配置及生成数据相对基线无差异。生成数据树仍为 `50d19016a8de31c504f73e2001c4d19fd203acba`。

## Markdown 与链接

- 使用 GitHub Markdown API 渲染未发布的 README：一个一级标题、两个表格、包含代码块的折叠目录和末尾引用块正常。
- 渲染检查发现新标签中将中文冒号包在强调标记内会露出原始星号；已把这些标点移到强调标记之外，复查无残留原始加粗标记。
- API 渲染片段本身不注入页面锚点；两个导航目标均与唯一的同名标题匹配，并从实际 GitHub 页面核验 `快速开始`、`长期目标` 的现有锚点。没有为适配检查而改写用户的标题。
- README 的仓库相对链接均存在；9 个致谢仓库均可访问；Issue #1 仍为 OPEN。
- 校验和渲染聊天只使用仓库结构示例，HTML 留在被忽略的 `.work/readme-archive-onboarding.owaEK0/chat.html`，没有提交示例派生副本。

## Checkpoint 与交付边界

- 主修改：`08b48bf5ac7b2c6bcb243aa87854c0fd9a736157` — `docs(readme): clarify archive onboarding and evidence sources`。包含 README、文档测试、本轮完整请求与有效计划。
- 本完成记录以独立的本地提交保存；其提交号由交付时的 `git log` 核验，不在文件中写入自引用 SHA。
- 本轮没有 push、PR、merge、Release 或部署，没有修改 GitHub About、Website、Topics 或此前未保存的首页模块设置。
- 远端 `main` 仍为 `903bdd51b3391dd6e85399c5bfdae6b2bb5922d6`；本地 `main` 保持 `de7605f`。新 README 和测试修复尚未进入公开默认分支，不能将本地测试通过描述为远端 CI 已恢复。
- 已向用户说明聊天工具的真实边界、Computer History 的可选性质与未读取实际活动，以及本轮仅本地交付的状态。
