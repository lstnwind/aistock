import numpy as np

# 将 kline_data 转换为 NumPy 数组
kline_data = np.array([
    [100, 120, 90, 110],  # 第一根K线
    [110, 130, 95, 105],  # 第二根K线
    [105, 115, 88, 98]    # 第三根K线
])

# 计算历史最高价
historical_max = np.max(kline_data[:, 1])  # 第二列是最高价

# 应用归一化
normalized_data = kline_data / historical_max

# 将归一化后的特征合并为一维向量
flattened_data = normalized_data.flatten()

print("原始K线数据：")
print(kline_data)
print("\n历史最高价：", historical_max)
print("\n归一化后的数据：")
print(normalized_data)
print("\n合并为一维向量：")
print(flattened_data)

