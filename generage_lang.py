import openai

# 在OpenAI平台上创建一个帐户，获取API密钥
api_key = "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"
openai.api_key = api_key

# 示例K线模式数据
k_line_data = ["大阳线", "小阴线", "中阳线", "大阴线", "小阳线", "中阴线", "大阳线", "小阳线", "中阳线", "大阳线"]

# 将K线数据转换为文本形式
text_data = " ".join(k_line_data)

# 使用GPT-3.5生成新的K线模式
response = openai.Completion.create(
    engine="text-davinci-003",  # 选择适用于文本生成的引擎
    prompt=text_data,
    max_tokens=50,  # 设置生成的最大标记数
    n=1  # 设置生成的示例数
)

# 提取生成的文本
generated_text = response['choices'][0]['text']

# 打印生成的K线模式
print("生成的K线模式:", generated_text)
