# 贡献记录

SZTU Connect 不设置固定治理角色。任何人都可以 clone、fork、补充来源、建立记录或提出更正；仓库历史、来源链和确定性检查共同构成审计轨迹。

## 最小贡献

一条可合并的记录只需要：

1. 合法取得、可描述的来源记录；
2. 不虚构精度的时间；
3. 一条或多条明确区分 `fact`、`memory`、`allegation`、`interpretation`、`uncertain` 的论断；
4. 每条事实性论断对应的来源和定位信息；
5. 对其他记录的关系（若有）；
6. `sztu-connect check --json` 通过。

可以从 `examples/minimal/` 复制结构，或让 Codex 使用 `record-campus-event` skill 起草。没有长篇 Markdown 叙事也可以先提交结构化记录。

## 更正而非静默改写

- 新来源补强原论断：追加引用。
- 来源相互冲突：保留双方，使用 `contradicts` 并把记录标为 `contested`。
- 原记录有误：在新提交中说明修改原因；Git 历史保留旧版本。
- 记录之间的关系只写正向一份，反向链接由构建器生成。

## 普通个人信息

与事实核查有关的姓名、公开职务、日期、公开机构联系方式可以原样记录。电话、邮箱、学号样式、聊天昵称等会产生提示，但不会自动使检查失败。秘密、完整证件号、身份接管信息、私人精确住址和实时位置必须从公开副本移除。

## 本地材料

不要直接执行或改动投稿文件。先清点：

```bash
sztu-connect ingest /path/to/materials --dry-run --json
```

报告写入 `.work/`，可能包含本地路径，不得提交。

## 提交前

```bash
sztu-connect check --json
python -m unittest discover -s tests
git diff --check
```

GitHub Pull Request 是一种协作方式，不是数据格式或本地使用的前提。
