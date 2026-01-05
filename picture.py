# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:35:39 2024

@author: 28154
"""

import pandas as pd

df = pd.read_excel('2020-2023data.xlsx')
df

df.info()

# 删除价格和原价列的¥
df['价格'] = df['价格'].str.replace('¥', '')
df['原价'] = df['原价'].str.replace('¥', '')

# 删除评论数列的“条评论”
df['评论数'] = df['评论数'].str.replace('条评论', '')
# 删除折扣列的“折”字
df['折扣'] = df['折扣'].str.replace('折', '')

# In[5]:


# 将每一步的处理变成数值类型
df['价格'] = df['价格'].astype(float)
df['原价'] = df['原价'].astype(float)
df['折扣'] = df['折扣'].astype(float)
df['评论数'] = pd.to_numeric(df['评论数'], errors='coerce')

# In[6]:


# 将出版年份转成时间格式
df['出版年份'] = pd.to_datetime(df['出版年份'])

# # 描述性统计
# In[7]:

print('df数据初步处理后的显示')
df.describe().T
# In[8]:
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df['出版年份'] = df['出版年份'].astype(str).str.extract('(\d{4})').astype(int)
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置字体为SimHei
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
matplotlib.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 数据统计：针对我们关心的年份，统计其出版的书籍数量
selected_years = [2020, 2021, 2022, 2023]
publication_counts = df[df['出版年份'].isin(selected_years)].groupby('出版年份').size()

# 设置图表风格（可选）
plt.style.use('seaborn-v0_8-darkgrid')  # 使用Seaborn的darkgrid风格

# 绘制折线图
fig, ax = plt.subplots(figsize=(12, 8))
line, = ax.plot(publication_counts.index, publication_counts.values, marker='o', linestyle='-', color='tab:blue',
                label='书籍数量')

# 添加阴影效果（可选）
ax.fill_between(publication_counts.index, publication_counts.values, color='tab:blue', alpha=0.3)

# 设置图表标题和轴标签
ax.set_title('特定年份书籍分布情况（2020-2023）', fontsize=16, fontweight='bold')
ax.set_xlabel('出版年份', fontsize=14)
ax.set_ylabel('书籍数量', fontsize=14)

# 设置网格线（可选）
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# 设置x轴刻度标签的旋转角度和字体大小
ax.set_xticks(publication_counts.index)
ax.set_xticklabels(publication_counts.index, rotation=45, fontsize=12)

# 添加图例
ax.legend(loc='upper left', fontsize=12)

# 添加文本注释（可选）
for i, (year, count) in enumerate(publication_counts.items()):
    ax.text(year, count + 1, f'{count}', ha='center', fontsize=12, color='tab:red')

# 优化布局（可选）
plt.tight_layout()

# 显示图表
plt.show()