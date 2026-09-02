# 事实核查

## 核查单位

核查对象是 `Claim`，不是整篇文章的单一“真假”标签。记录可以同时包含已支持事实、个人回忆、相互冲突的陈述和编辑解释。

| `kind` | 含义 |
|---|---|
| `fact` | 可以由来源直接核查的陈述 |
| `memory` | 某个来源对经历的回忆；回忆存在本身可核查，不等于全部细节已证实 |
| `allegation` | 来源对他人或机构提出的待核主张 |
| `interpretation` | 基于已列事实的解释 |
| `uncertain` | 无法确定或证据不足的陈述 |

## 证据角色

- `supports`：来源直接支持该论断。
- `contradicts`：来源与该论断冲突。
- `context`：提供背景，但不能独立证明论断。

`locator` 应尽可能精确。网页可写标题锚点或原句附近小标题，PDF 写页码，聊天写消息 ID，音视频写时间码。不要用 AI 摘要代替 locator。

## 记录状态

- `draft`：结构尚未完整。
- `source-backed`：事实性论断至少有支持来源。
- `corroborated`：每条事实性论断有至少两个不同 independence group 的支持来源。
- `contested`：至少存在一条 `contradicts` 引用。
- `withdrawn`：正文不再作为当前记录呈现，但保留最小说明和 Git 历史。

状态由证据关系约束，不由贡献者身份或固定角色决定。`source-backed` 表示记录中的事实性论断有来源，不等于项目宣告其为终局真相。

当单一来源只是在陈述某件事，Claim 应准确写成“该来源称……”或选择 `memory`、`allegation`、`uncertain`，不能把“来源确实这样写”直接改写成“现实中确定发生”。明确虚构、合成或测试材料不得进入正式 Event／Source 索引。

## 更正

新增证据时追加 Citation；证据冲突时并列保存；事实关系变化时可用 `corrects`、`supersedes` 或 `disputes` Link 指向相关记录。不要为了获得整齐结论而删除主要反证，也不要把向量召回的相似文本当作独立证据。

## 推荐核查输出

Agent 执行 `fact-check-event` skill 时，输出至少包括：

```text
claim_id
claim_text
claim_kind
record_time
supporting_sources_and_locators
contradicting_sources_and_locators
source_independence
unresolved_questions
possible_correction
```

报告描述证据矩阵，不分派治理角色，不把“尚未证实”误写为“已经证伪”。
