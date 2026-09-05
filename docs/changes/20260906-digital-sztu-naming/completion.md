# 实施记录

## 已完成

- 从 `61db849940009537f3ee2a5c0b392109096863a0` 提取独立的命名兼容更新，包与插件版本为 `0.1.1`。v0.2 档案、普查和图谱仍在独立升级分支。
- 包名、插件标识、主命令统一为 `digital-sztu`，主模块为 `digital_sztu`；旧命令、模块和初始化 Skill 使用同一实现。
- 同步 README、安装指南、初始化检测、插件清单、Makefile、PR 模板和 CI；保留用户的 README 段落结构及后文“构史”。
- Schema URN、既有 chunk ID、v0.1 JSON 契约与第三方源码存档未重命名。新导出的 exporter 标记为 digital-sztu，旧值继续可读。
- GitHub 仓库已更名为 `Shuang-su/digital-sztu`，API 读回 ID 仍为 `1354678557`；共享 origin 已更新为新 HTTPS 地址。

## 验证

- 120 项单元测试通过，默认跳过 2 项平台集成测试；额外启用 macOS 集成后 38 项初始化测试全部通过。
- 实际构建并安装 `digital_sztu-0.1.1-py3-none-any.whl`，确认使用 site-packages 中的安装包；两种命令和两种模块启动方式返回一致的 doctor 结果。
- 新旧命令连续构建，12 个派生文件哈希完全一致，且没有相对主分支的生成数据差异。
- 插件清单与新旧初始化 Skill 校验通过；第三方源码存档离线校验通过，没有运行上游代码。
- `check --json`、旧入口校验与 `git diff --check` 通过。
- 第一次插件校验使用系统 Python 时缺少 PyYAML；改用任务内已经具备该依赖的虚拟环境后通过，未修改全局依赖。

## 待核验

提交后推送命名 PR，等待服务端 CI，正常合并并快进常用工作副本，再验证本地升级安装。当前未发布 PyPI 包或 GitHub Release；本项目继续按仓库源码安装，wheel 作为本地验证产物。
