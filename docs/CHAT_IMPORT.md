# 聊天导出

v0.1 只有平台无关 JSONL Schema、校验和通用 HTML renderer；没有微信数据库解析、解密、密钥提取或自动 normalizer。

Agent 可以在用户明确提供合法导出文件时，按 `schemas/chat-message.schema.json` 映射字段。保留原时间、消息 ID、回复关系和可核查显示名；不需要默认匿名化。若使用化名、最小化或脱敏，必须在字段中明确表示，不能把处理后的文本冒充原文。

```bash
sztu-connect validate-chat examples/chat/messages.example.jsonl --json
sztu-connect render-chat examples/chat/messages.example.jsonl \
  --title "结构示例" \
  --output .work/chat/example.html \
  --json
```

聊天中的陈述是来源内容，不会自动成为 `fact`。创建事实记录时仍需建立 Claim、Citation 和 locator（通常为消息 ID）。
