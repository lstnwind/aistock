from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
from K_word import classify_kline
# 读取CSV文件
file_path = './300103.csv'
df = pd.read_csv(file_path)

# 示例K线数据
kline_data = df[['open', 'high', 'low', 'close']].values.tolist()

# 初始化前一日收盘价为None
prior_close = None

# 将K线数据映射到形态
kline_types = []
for open_price, high_price, low_price, close_price in kline_data:
    kline_type = classify_kline(open_price, high_price, low_price, close_price, prior_close)
    kline_types.append(kline_type)
    # 更新前一日收盘价
    prior_close = close_price

# 独热编码形态特征
encoder = OneHotEncoder()
kline_types_encoded = encoder.fit_transform(pd.DataFrame(kline_types, columns=['kline_type'])).toarray()

# 标签化形态标签
label_encoder = LabelEncoder()
kline_labels_encoded = label_encoder.fit_transform(kline_types)

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(kline_types_encoded, kline_labels_encoded, test_size=0.2, random_state=42)

# 打印编码后的结果
print("编码后的形态特征：")
print(pd.DataFrame(kline_types_encoded, columns=encoder.get_feature_names_out(['kline_type'])).head())

print("\n标签化后的形态标签：")
print(label_encoder.classes_)
