# 最终实施计划

## 目标

把原 v0.1 草案改造成可直接开始记录事件的 SZTU Connect Codex plugin，并以事件而不是时间或人物为唯一事实中心。

## 数据结构

1. Event 保存一次：时间、Claim、Citation、正向 Link、隐私索引选择和 provenance。
2. Person、Organization、Place、Institution、Topic 使用轻量 Node，只保存稳定 ID、名称、别名和必要说明，不手写 Event 列表。
3. Source 为每条 Claim 提供 `supports`、`contradicts`、`context` 角色与精确 locator。
4. Collection 使用相同 Event IDs 组织编年体、纪传体、典制体和纪事本末体／专题。
5. Markdown 支持 `[[id|label]]` 导航；证据关系仍以 Event JSON 为准。

## 自动关联与双向链接

1. `record-campus-event` skill 接收用户提供的一个事件及来源。
2. Agent 搜索既有 Event、Source 与 Node；只复用明确身份匹配，歧义不强行合并。
3. 新对象可以建立 `status: stub` Node。
4. Event 只写单向 Link；构建器生成目标的 incoming backlink。
5. 构建器按人物、组织、地点、制度、主题和年份生成目录索引，并生成 Graph、Timeline 与 Collection 视图。

## Agent plugin

1. 仓库根提供 `.codex-plugin/plugin.json`，唯一技能目录为 `skills/`。
2. v0.1 定位为 instruction-only Skills + 本地 Python CLI。
3. Manifest 不声明不存在的 MCP Server、WebMCP、App、网页抓取、平台解析或自动发布能力。
4. 所有输出路径限制在 `.work/` 或确定的 `data/generated/`。

## 向量知识库

1. 生成供应商无关的 `knowledge/chunks.jsonl` 与 manifest。
2. Chunk 覆盖 Event summary、Claim、Node metadata、Collection summary、Source metadata。
3. 稳定 `chunk_id` 表示逻辑位置，`revision_id` 表示内容修订。
4. 每个 Claim chunk 保留 Citation、Event 时间、History form、核查状态及只属于该 Claim 的证据关系；Event summary 保留全局反链。
5. Embedding 不在构建时联网，默认只写 `.work/` sidecar。

## 隐私与事实核查

1. 姓名、公开职务、日期和事实必要上下文不自动脱敏。
2. Token、Cookie、私钥、完整证件号、身份接管信息、私人精确住址和实时位置为硬阻断。
3. 电话、邮箱、学号样式、房间等为 review 提示；默认不让检查失败。
4. 取消固定治理角色、两人审核、强制 `privacy.reviewed` 与 CODEOWNERS。
5. Corroboration 只统计不同 independence group 的 `supports`，不统计反证、上下文或复制来源。

## 质量与发布

1. 正式内容目录保持空白；所有虚构结构示例放在 `examples/minimal/`。
2. 校验真实日历日期、时间精度、路径年份、引用目标、Claim ID、Link target、Wikilink target、Collection form 与隐私索引边界。
3. 连续两次 build 必须逐字节一致。
4. 校验 Plugin、所有 Skills、CLI、单元测试、隐私扫描、Git diff 与生成物。
5. 初始化 Git main，创建本地 checkpoint；随后创建并 push 到公开个人仓库 `Shuang-su/sztu-connect`。
6. 本次不创建 PR、tag、release、部署、MCP/WebMCP runtime、网站或远程向量服务。
