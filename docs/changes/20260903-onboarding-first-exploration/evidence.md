# 实施依据与边界

核对日期：2026-09-03。

## 当前仓库与关联任务

- 工作分支 `codex/agent-first-onboarding`，起点 `0ed2a081f1a202b33a3b6cf98c19130b75d5b1c0`，开始时工作树干净。
- `git ls-remote origin HEAD refs/heads/main` 读回 `621de40f2fed1d2345b2e8bff1d7797962072150`，与本地 main / origin/main 相同，没有新的网页 README 编辑需要合入。
- “添加可信来源工具存档”已交付且已被当前分支包含：固定源码、许可和登记表；CipherTalk 图形安装包仍使用固定上游下载入口，WeChatMsg 是历史源码备份。本轮未重新存档、改版本、下载或执行它们。详情见 [该任务完成记录](../20260903-chat-tool-archives/completion.md)。
- 基础初始化及 109 项既有验证的上下文见 [上一阶段记录](../20260903-agent-first-onboarding/completion.md)；本轮重新执行检查，不以旧通过状态替代当前结果。

## 第一方能力依据

| 依据 | 用于本轮的判断 | 不据此宣称 |
|---|---|---|
| [Computer Use](https://learn.chatgpt.com/docs/computer-use) | 原生入口、应用授权与系统权限分别处理；图形步骤可用时采用 | 九种客户端有相同工具，或可自动代为确认安全弹窗 |
| [Computer History](https://learn.chatgpt.com/docs/customization/computer-history) | 个人启用、平台 / 账号条件、暂停与恢复、已有范围保留 | 初始化 Python 脚本能启用采集，或 Windows / 其他客户端必然支持 |
| [历史保留与数据处理](https://learn.chatgpt.com/docs/customization/computer-history#privacy-and-local-storage) | 原始事件窗口与长期保留摘要分开核对，回到原件取证 | 全部人生历史可恢复，或本地文件意味着完全离线处理 |

以上为官方文档阅读与本地接口核对，不是实际使用用户历史的数据验证。没有读取真实 Computer History 状态、设置或事件，没有安装或开启 Computer Use / Computer History。

## 已知集成边界

- 用户入口包含广泛文件访问授权，但同一批准计划又明确限定首次候选发现范围；本轮保留入口原文，在指南解释默认范围，不重新定义全局内容校验策略。
- 旧 README / 隐私文档的正式材料公开规则与部分工具 Skill 的授权说明存在既有差异。本轮只明确首次探索不会自动建正式记录或公开提交，不扩大为重写隐私策略；真实材料发布仍须另行核对具体授权和适用边界。
- 九种客户端及真实应用安装的待验收状态保持不变；合成案例不能替代原生权限窗口、账号条件、宿主机或跨平台验收。
