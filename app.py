# Streamlit Beauty Analyzer (Stable Demo Version)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 页面设置
st.set_page_config(page_title="Beauty Analyzer", layout="wide")
st.title("Beauty Ingredients & User Preference Analyzer")
st.caption("Demo Version: Using simulated Sephora data for demonstration")

# --------------------------
# 1. 生成长度一致的模拟数据
# --------------------------
@st.cache_data
def generate_demo_data():
    # 统一生成100条数据
    n = 100
    categories = ["Skincare", "Makeup", "Haircare", "Fragrance"] * (n // 4 + 1)
    categories = categories[:n]
    
    prices = [10, 25, 40, 60, 80, 100] * (n // 6 + 1)
    prices = prices[:n]
    
    ratings = [3.5, 4.0, 4.2, 4.5, 4.7, 5.0] * (n // 6 + 1)
    ratings = ratings[:n]
    
    ingredients_list = [
        "Hyaluronic Acid, Niacinamide, Vitamin C",
        "Retinol, Salicylic Acid, Glycolic Acid",
        "Ceramide, Aloe Vera, Shea Butter",
        "Tea Tree Oil, Vitamin E, Peptides"
    ]
    ingredients = ingredients_list * (n // 4 + 1)
    ingredients = ingredients[:n]
    
    data = {
        "category": categories,
        "price": prices,
        "rating": ratings,
        "ingredients": ingredients
    }
    return pd.DataFrame(data)

df = generate_demo_data()
st.success("✅ 数据加载成功（演示模式）")

# --------------------------
# 2. 侧边栏筛选
# --------------------------
st.sidebar.header("Filter Panel")
category = st.sidebar.selectbox("Category", df["category"].unique())
price_range = st.sidebar.slider("Price Range", int(df["price"].min()), int(df["price"].max()), (10, 60))
rating_filter = st.sidebar.slider("Min Rating", 0.0, 5.0, 3.5)

# 筛选数据
df_filter = df[
    (df["category"] == category) &
    (df["price"] >= price_range[0]) &
    (df["price"] <= price_range[1]) &
    (df["rating"] >= rating_filter)
]

# --------------------------
# 3. 成分分析图表
# --------------------------
st.subheader("1. Top Popular Ingredients")
# 统计成分出现次数
ingred_list = []
for item in df_filter["ingredients"]:
    ingred_list.extend([i.strip() for i in item.split(",")])
ingred_count = pd.Series(ingred_list).value_counts().head(10)
st.bar_chart(ingred_count)

# --------------------------
# 4. 价格 vs 评分散点图
# --------------------------
st.subheader("2. Price vs Rating Correlation")
fig, ax = plt.subplots()
ax.scatter(df_filter["price"], df_filter["rating"], alpha=0.6, color="#FF6B6B")
ax.set_xlabel("Price (USD)")
ax.set_ylabel("User Rating")
ax.set_title("Price vs Rating of Selected Products")
st.pyplot(fig)

# --------------------------
# 5. 成分词云
# --------------------------
st.subheader("3. Ingredients Word Cloud")
text = " ".join(ingred_list)
wc = WordCloud(width=600, height=300, background_color="white", colormap="viridis").generate(text)
fig_wc, ax_wc = plt.subplots()
ax_wc.imshow(wc, interpolation="bilinear")
ax_wc.axis("off")
st.pyplot(fig_wc)

# --------------------------
# 6. 核心洞察
# --------------------------
st.subheader("4. Key Insights")
st.markdown("""
- **高人气成分**：玻尿酸、烟酰胺、维生素C是最常见的热门成分
- **价格与评分**：中低价（$10-$60）产品普遍评分更稳定，高单价产品不一定代表更好口碑
- **成分趋势**：保湿和修复类成分在护肤产品中占比最高
""")

st.balloons()
