from collections import defaultdict
from K_word import classify_kline
import pandas as pd

# 读取CSV文件
file_path = './300103.csv'
df = pd.read_csv(file_path)

# 显示数据的前几行
print(df.head())
def build_kline_dictionary(kline_data):
    kline_dict = defaultdict(int)
    prior_close = None  # 或者使用适当的初始值
    for i in range(len(kline_data)):
        # 获取当前K线的形态
        current_kline = classify_kline(*kline_data[i], prior_close)
        kline_dict[current_kline] += 1

        # 更新前一日收盘价
        prior_close = kline_data[i][3]

        # 二阶短语
        if i > 0:
            two_phrase = f"{classify_kline(*kline_data[i-1], None)} {current_kline}"
            kline_dict[two_phrase] += 1

        # 三阶短语
        if i > 1:
            three_phrase = f"{classify_kline(*kline_data[i-2], None)} {classify_kline(*kline_data[i-1], None)} {current_kline}"
            kline_dict[three_phrase] += 1

    return kline_dict

# 示例K线数据
kline_data = df[['open', 'high', 'low', 'close']].values.tolist()

# 初始化前一日收盘价为None
prior_close = None

# 构建K线字典
kline_dictionary = build_kline_dictionary(kline_data)

# 打印字典中的短语及其频率
for phrase, frequency in kline_dictionary.items():
    print(f"{phrase}: {frequency}次")
