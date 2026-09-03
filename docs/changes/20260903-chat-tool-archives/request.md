# 用户请求

日期：2026-09-03。项目：SZTU Connect。

## 最初请求，按原顺序

1. “https://github.com/mintleaf84/CipherTalk-SafeFork 为项目添加可信来源工具的存档，应该是在根目录下加个文件夹放；再看看 https://github.com/xaoyaoo/PyWxDump https://github.com/git-jiadong/wechatDataBackup https://github.com/LC044/WeChatMsg 有没有也可用的，或者其他存档版本，考虑加进来”
2. “要求‘Deep research’”
3. “本项目可执行的导入器”
4. “导入器就使用别人做好的，不要管其他，只要实现来源可信”
5. “CipherTalk-SafeFork的 https://github.com/mintleaf84/CipherTalk-SafeFork/releases/download/v2026.829.0/CipherTalk-2026.829.0-Setup.dmg 和exe版本你下载下来放文件夹并提供给其他用户；并优化更新我们仓库的相关skill、技能；其他项目你看一下支持版本和其他有没有比现在这个更好的”

## 讨论中的选择与修订

以下为后续确认的约束整理，不将概述冒充逐字引文：

1. 使用第三方已有工具，聚焦第一手聊天导出的来源可追溯性；不开发本项目的微信解析器、解密器或新导出器。可追溯性不能包装成对聊天真实性或所有发言的保证。
2. 主要工具采用 CipherTalk，Windows 历史备用采用 WeChatMsg；仅在独立存档替代不足时再考虑把 PyWxDump / wechatDataBackup 加入实体存档。
3. 确认保留 CipherTalk 和 WeChatMsg 两份完整固定源码存档。
4. 曾考虑使用 Git LFS 托管超过 GitHub 普通 Git 单文件限制的安装包；该选择已被下一项替代。
5. **最终改为：DMG / EXE 使用固定上游 GitHub Release 直链。**本轮暂缓安装包下载与重托管，不配置 Git LFS；两份源码实体存档继续保留。
6. 优化仓库已有聊天相关技能与共享文档；其他项目核查版本、保存来源和是否更适合，不扩展为聊天解析开发。
7. 验证后创建本地 checkpoint，将本次变更集成到 main 并推送；不创建 PR、Release、tag 或部署。保护其他任务已做的 README 和记录规则修改，不混入无关改动。

## 最终确认

用户对最终方案回复：“可以的”。实施以 [最终计划](plan.md) 为准；最初下载并重托管安装包的要求已由上面的直链方案取代。

本次输入仅为公开工具项目与本仓库文件，不涉及真实聊天、账号或私人材料。工具保存与技能更新不构成取得其他人的账号、凭据、原始数据库或发布其私密信息的授权。
