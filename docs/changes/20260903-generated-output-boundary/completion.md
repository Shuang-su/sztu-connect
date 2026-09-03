# 完成记录

## 本地实施结果

- 将用户已有的六个文件原样保存为独立提交；没有把它们描述为本轮 Agent 新设计的内容规则。
- 本轮新增代码修改仅位于 `src/sztu_connect/build.py`，新增回归测试仅位于 `tests/test_repository.py`。
- 构建在任何生成文件写入前，统一拒绝 `data`、`data/generated`、`data/generated/directories`、`data/generated/knowledge` 中的符号链接，包括目标不存在的悬空链接。
- 检查失败返回包含 `ok: false` 和 `errors` 的结构化结果；不会创建部分时间线、覆盖外部同名输出文件或改动原有链接。
- 用户的扫描等级、正式记录准入、URL 字段、知识导出规则、Schema 与 README 文案均未被本轮边界修复回改。
- 按仓库约定补充完整的本轮请求、最终计划与本完成记录。

## 回归证据

先增加测试，再应用修复：

- 修复前，`knowledge`、`directories` 指向外部目录的两种情况均错误地返回成功，产生 2 个失败子用例。
- 修复前，`data` 及两个生成子目录为悬空链接时，产生 3 个未处理的文件系统异常；`data/generated` 自身的悬空链接已由原有检查覆盖。
- 修复后，同一组定向测试全部通过。新增的两个测试方法覆盖 6 个目录场景，并验证外部标记文件保持原字节、链接没有改变、失败前没有部分生成文件。
- 测试只使用临时示例仓库与合成标记内容，没有读取或写入用户的仓库外材料。

## 验证结果

| 检查 | 结果 |
|---|---|
| 两份配置的 JSON 解析 | 通过 |
| `sztu-connect doctor --json` | 通过，Python 3.13.5 |
| `sztu-connect validate --json` | 通过，无错误或警告 |
| 普通及 `--strict` 隐私扫描 | 通过，无扫描命中 |
| 普通及 `--strict` 综合检查 | 通过 |
| 两次 `sztu-connect build --json` | 通过 |
| 已跟踪生成文件的 SHA-256 比较 | 12 个文件在构建前后、两次构建之间完全一致 |
| `python -m unittest discover -s tests` | 53 项通过，包含原有 51 项及新增 2 项 |
| `python -m compileall -q src tests` | 通过 |
| 工作区与暂存区 `git diff --check` | 通过 |
| `git diff --exit-code -- data/generated` | 无变化 |

正式 Event、Node、Collection、Source 数量均仍为零。本轮没有加入真实原件、聊天导出文件、电脑活动记录或新的正式内容数据。另行核对了待推送的提交与文件；没有把放宽后的扫描退出码当作内容发布许可。

## 用户改动保留核验

以下 Git blob 与本轮开始时一致：

```text
README.md                          f5b89557782cbbba286fe1dc86fb7b494176567d
schemas/knowledge-chunk.schema.json c58337a09be21f32334e10ac39c3ba727f000cda
src/sztu_connect/knowledge.py       7ddc05e9fcc8a7870f3bb64bef38a9e7231318b0
src/sztu_connect/privacy.py         aa16efcbcaa8d5207db34b190df5fc839f2863e5
src/sztu_connect/validation.py      739d472f4cfb089bb5a69285333da8cb5d8611ee
```

其他已提交文档未被本轮修改。`build.py` 的后续差异只涉及输出目录预检；`test_repository.py` 只追加对应回归测试，不删除或改写用户已有断言。

## Checkpoint

- 本轮起点：`74ffa16ca0647a8851b47ae726c1c25254e86bf5`。
- 用户手动规则调整：`9ca0618728612166c973b7068d76bca1a3e8264d` — `feat(archive): checkpoint user-defined record and export rules`。
- 输出边界修复、测试、请求与计划：`0fac22c9628fb81dfda913d59ef9bd3ff2f86371` — `fix(build): guard every generated output directory`。
- 本完成记录单独提交，不在文件中循环引用其自身提交号。

## 发布授权与最终核验

用户明确要求提交、推送并合并。发布范围为当前 `codex/readme-archive-onboarding` 分支，包含先前已提交的 README 与文档变更、用户的规则调整和本轮边界修复。

本文件记录截至本地 checkpoint 的实施与验收结果，生成本记录时尚未确认远端发布成功。后续须普通推送分支、通过 PR 检查后以 merge commit 合并至 `main`，再回读 PR、远端 SHA 与 `main` 检查。实际推送、合并及远端检查结果以对应 GitHub 记录和本轮最终交付回复为准，不从本地测试通过推断远端成功。

本次不修改 GitHub About，不创建 Release、部署或新 Issue，不删除分支，不强推或改写历史，也不修改 `.work/` 的 CLI 输出约束。该补丁解决已复现的固定生成目录符号链接越界，不扩展为其他内容规则或操作系统沙箱改造。
