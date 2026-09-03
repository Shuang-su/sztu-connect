# 上手流程发布检查记录

日期：2026-09-03。

## 用户请求

> 以后记得自动推送
> 这次推送并合并

该请求在本地实现完成后给出，明确授权本次推送和合并。今后自动推送是提出请求者的个人开发交付偏好，已单独保存；不将它改写为本项目为所有用户自动发布材料的行为，也不据此默认自动合并、部署或发布版本。

## 范围与执行计划

- 发布分支：`codex/agent-first-onboarding`，本地交付点 `85b48d535325f13a5378699726a7e5e8fede51b6`。
- 目标仓库：`Shuang-su/sztu-connect`，默认分支 `main`；发布前 fetch 后为 `621de40f2fed1d2345b2e8bff1d7797962072150`。
- 发布两阶段已完成的初始化助手、README / 共用指引、首次探索 Skill、测试及变更记录；不重新修改品牌文案、正式内容、Schema、导出格式或固定工具存档。
- 核对干净工作树及远端后普通推送，通过 PR 等待项目检查；使用 merge commit 保留原有提交，不强推或使用管理员开关绕过检查。
- 合并后核对服务端 PR 状态、默认分支 SHA、默认分支 CI，以及 README 与公开上手 URL；本地只做安全的快进同步，保留工作分支。

## 已完成的发布前核验

- 起始工作树干净，远端和默认分支正确；没有本地私人材料或测试输出进入跟踪文件。相对 `origin/main` 的正式数据、Schema、内容工具实现、依赖锁和既有 `importers/` 无差异。
- 本地 `sztu-connect check --json` 通过，隐私扫描继续为 `block: 0 / review: 6`；已有正式数据与构建结果不变。`git diff --check` 通过。
- 分支已普通推送，服务端 HEAD 为 `85b48d535325f13a5378699726a7e5e8fede51b6`，建立 [PR #4](https://github.com/Shuang-su/sztu-connect/pull/4)。没有重复 PR。
- [首轮 Checks](https://github.com/Shuang-su/sztu-connect/actions/runs/33733219921) 三个作业均为 `success`。合并检查返回 `MERGEABLE / CLEAN`；未发现行级审查评论。Cursor Bugbot 检查为中性 / skipping，不冒充已完成主动人工审查。

| 作业 | 实际环境与测试 | 结果 |
|---|---|---|
| `check` | Ubuntu 24.04，Python 3.13.15；离线源码存档、内容校验、117 项单测、双构建 / 派生文件检查 | 成功，单测按平台跳过 2 项 |
| `Bootstrap (macos-latest)` | `macos-26-arm64`，Python 3.13.14；38 项 bootstrap 与 7 项报告边界测试 | 成功，Windows junction 按平台跳过 1 项 |
| `Bootstrap (windows-latest)` | Windows Server 2025，Python 3.13.15；38 项 bootstrap 与 7 项报告边界测试 | 全部通过，包括真实 junction 边界测试 |

据实际日志更新 [验收矩阵](../../ONBOARDING_TEST_MATRIX.md)，只把 CI 核心验证改为已执行；九种客户端的真实完整体验、聊天应用安装、Computer History 采集与权限窗口仍待验证。文档补记形成新提交后，仍须检查最终 HEAD，不把上一提交的绿灯当作最终提交的结果。

## 后续结果的位置

本文记录发布请求和合并前已经取得的证据，不预写尚未发生的合并。最终合并 SHA、目标分支状态及后续检查以 [PR #4](https://github.com/Shuang-su/sztu-connect/pull/4) 和仓库 Actions 的服务端记录为准；默认分支 README 与上手 URL 在合并后另行核对。
