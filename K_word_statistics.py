from collections import defaultdict
import pandas as pd

def generate_k_line_phrases(data):
    phrases = []
    for i in range(len(data) - 2):
        k_line_pattern = (
            data.iloc[i]['K_line_type'],
            data.iloc[i + 1]['K_line_type'],
            data.iloc[i + 2]['K_line_type']
        )
        phrases.append(k_line_pattern)
    return phrases

# 示例数据，假设data是一个包含K线类型的DataFrame
data = pd.DataFrame({
    'Date': pd.date_range(start='2022-01-01', periods=10),
    'Open': [100, 105, 110, 95, 98, 102, 108, 112, 110, 115],
    'High': [105, 110, 115, 100, 105, 112, 115, 120, 118, 120],
    'Low': [98, 100, 105, 90, 94, 98, 105, 108, 108, 110],
    'Close': [102, 108, 112, 98, 100, 105, 110, 115, 112, 118],
})

# 假设你已经有了分类好的K线类型数据
data['K_line_type'] = ["大阳线", "小阴线", "中阳线", "大阴线", "小阳线", "中阴线", "大阳线", "小阳线", "中阳线", "大阳线"]

# 生成K线短语序列
k_line_phrases = generate_k_line_phrases(data)

# 统计词频
phrase_freq = defaultdict(int)
for phrase in k_line_phrases:
    phrase_freq[phrase] += 1

# 打印词频字典
print("词频字典:")
for key, value in phrase_freq.items():
    print(f"{key}: {value}")
