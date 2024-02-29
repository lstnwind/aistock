import pandas as pd

# 读取CSV文件
file_path = './300103.csv'
df = pd.read_csv(file_path)

# 显示数据的前几行
print(df.head())
def classify_kline(open_price, high_price, low_price, close_price, prior_close_price):
    # 判断开盘类型
    if prior_close_price is None:
        opening_type = "平开"
    elif open_price > prior_close_price:
        opening_type = "高开"
    elif open_price == prior_close_price:
        opening_type = "平开"
    else:
        opening_type = "低开"

    # 判断影线类型
    upper_shadow = high_price - max(open_price, close_price)
    lower_shadow = min(open_price, close_price) - low_price
    kline_shiti = abs(close_price-open_price)
    if upper_shadow == 0 and lower_shadow == 0:
        shadow_type = "光头光脚"
    elif upper_shadow == 0:
        shadow_type = "秃顶"
    elif lower_shadow == 0:
        shadow_type = "赤脚"
    elif upper_shadow > lower_shadow and upper_shadow > kline_shiti:
        shadow_type = "长上影"
    elif upper_shadow < lower_shadow and lower_shadow > kline_shiti:
        shadow_type = "长下影"
    else:
        shadow_type = "纺锤体"

    # 判断实体类型
    price_change_percentage = abs((close_price - open_price) / open_price)
    if close_price > open_price:
        if price_change_percentage > 0.05:
            body_type = "大阳线"
        elif 0.03 < price_change_percentage <= 0.05:
            body_type = "中阳线"
        else:
            body_type = "小阳线"
    elif close_price < open_price:
        if price_change_percentage > 0.05:
            body_type = "大阴线"
        elif 0.03 < price_change_percentage <= 0.05:
            body_type = "中阴线"
        else:
            body_type = "小阴线"
    else:
        body_type = "星线"

    # 连接开盘类型、影线类型和实体类型
    combined_type = f"{opening_type} {shadow_type} {body_type}"

    return combined_type

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

# 将生成的 kline_types 合并到原始 DataFrame
df['kline_types'] = kline_types

# 打印合并后的 DataFrame 的前20行
print(df.tail(20))
