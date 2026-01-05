

import pandas as pd
df = pd.read_excel('当当网图书畅销榜近四年榜单数据.xlsx')

df.info()

# # 数据处理


# 删除价格和原价列的¥
df['价格'] = df['价格'].str.replace('¥', '')
df['原价'] = df['原价'].str.replace('¥', '')
# 删除评论数列的“条评论”
df['评论数'] = df['评论数'].str.replace('条评论', '')
# 删除折扣列的“折”字
df['折扣'] = df['折扣'].str.replace('折', '')


# 将每一步的处理变成数值类型
df['价格'] = df['价格'].astype(float)
df['原价'] = df['原价'].astype(float)
df['折扣'] = df['折扣'].astype(float)
df['评论数'] = pd.to_numeric(df['评论数'], errors='coerce')

# 将出版年份转成时间格式
df['出版年份'] = pd.to_datetime(df['出版年份'])

print('df数据初步处理后的显示')
#df.describe().T


# # 可视化分析

# ## 每年评论数最高的作者

max_comments_author = df.groupby('年份')['评论数'].idxmax().apply(lambda x: df.loc[x]['作者'])
print(max_comments_author)

import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


max_comments = df.groupby('年份')['评论数'].max()
max_comments_author = df.loc[df.groupby('年份')['评论数'].idxmax()]['作者']
plt.bar(max_comments_author, max_comments)
for i, v in enumerate(max_comments):
    plt.text(i, v + 10000, str(v), ha='center', va='bottom', fontsize=8)
plt.xlabel('作者')
plt.ylabel('评论数')
plt.title('每年评论数最高的作者及其评论数')
plt.show()


# ## 不同价格区间的书籍数量分布


import numpy as np
price_range = pd.cut(df['价格'], bins=[0, 50, 100, 150, np.inf], right=False)
price_counts = price_range.value_counts()
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(price_counts, labels=price_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors, wedgeprops=dict(width=0.4))
bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

plt.axis('equal')
plt.title('不同价格区间的书籍数量分布', fontsize=16, y=1.1)
plt.show()


# ## 价格排名前10的书籍

top_10_books = df.sort_values(by='价格', ascending=False).head(10)
plt.figure(figsize=(10, 8))
plt.barh(top_10_books['书名'], top_10_books['价格'], color='skyblue')
plt.xlabel('价格')
plt.ylabel('书名')
plt.title('价格排名前10的书籍')
plt.gca().invert_yaxis()
plt.show()


# ## 相关性分析

book_data = df[['排名', '价格', '原价', '评论数']]
correlation_matrix = book_data.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, square=True, fmt='.2f')
plt.title('图书排名与价格、原价、评论数的相关性热力图')
plt.show()


# ## 作者词云图


from wordcloud import WordCloud
import matplotlib.pyplot as plt
word_frequency = df.groupby('作者')['评论数'].sum().reset_index()
word_frequency_dict = dict(zip(word_frequency['作者'], word_frequency['评论数']))
wordcloud = WordCloud(font_path='simhei.ttf', width=800, height=400, background_color='white').generate_from_frequencies(word_frequency_dict)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('作者评论数词云图')
plt.show()



