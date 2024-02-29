from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import OneHotEncoder
import pandas as pd


# 生成并保存所有126种K线形态到TXT文件
with open("all_kline_types.txt", "w") as file:
    for opening_type in ["平开", "高开", "低开"]:
        for shadow_type in ["光头光脚", "秃顶", "赤脚", "等长上下影", "长下影", "长上影"]:
            for body_type in ["大阳线", "中阳线", "小阳线", "星线", "大阴线", "中阴线", "小阴线"]:
                kline_type = f"{opening_type} {shadow_type} {body_type}"
                file.write(f"{kline_type}\n")

# 读取包含K线形态的文本文件
with open('all_kline_types.txt', 'r', encoding='gbk') as file:
    kline_patterns = [line.strip() for line in file]

# 打印列表内容
print(kline_patterns)



# 使用CountVectorizer进行分词
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(kline_patterns)

# 获取特征词列表
feature_names = vectorizer.get_feature_names_out()

# 将稀疏矩阵转换为数组
X_array = X.toarray()

# 创建DataFrame来显示编码后的K线形态
df_encoded = pd.DataFrame(X_array, columns=feature_names)

# 使用OneHotEncoder进行独热编码
encoder = OneHotEncoder(sparse=False, drop='first')
X_encoded = encoder.fit_transform(df_encoded)

# 创建DataFrame来显示独热编码后的K线形态
df_onehot = pd.DataFrame(X_encoded, columns=encoder.get_feature_names_out(feature_names))
print(df_onehot)