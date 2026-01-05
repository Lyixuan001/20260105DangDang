# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:35:39 2024

@author: 28154
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 读取数据
df = pd.read_excel('2020-2023data.xlsx')

# 数据预处理（删除不需要的字符，转换数据类型）
df['价格'] = df['价格'].str.replace('¥', '').astype(float)
df['原价'] = df['原价'].str.replace('¥', '').astype(float)
df['评论数'] = df['评论数'].str.replace('条评论', '').apply(pd.to_numeric, errors='coerce')
df['折扣'] = df['折扣'].str.replace('折', '').astype(float)

if df['出版年份'].dtype == object:  # 检查是否为对象类型（通常是字符串）
    df['出版年份'] = df['出版年份'].astype(str).str.extract('(\d{4})').astype(int)
elif df['出版年份'].dtype not in [int, float]:  # 如果不是整型也不是我们假设的字符串格式，则抛出警告
    raise ValueError("出版年份的格式不符合预期，请检查数据！")

# 设置字体为SimHei（确保该字体在您的系统上可用）
rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 数据统计：统计所有年份出版的书籍数量
publication_counts = df.groupby('出版年份').size()

# 设置图表风格（可选）
plt.style.use('seaborn-v0_8-darkgrid')  # 使用Seaborn的darkgrid风格

# 绘制折线图
fig, ax = plt.subplots(figsize=(12, 8))
line, = ax.plot(publication_counts.index, publication_counts.values, marker='o', linestyle='-', color='tab:blue', label='The number of books')

# 添加阴影效果（可选）
ax.fill_between(publication_counts.index, publication_counts.values, color='tab:blue', alpha=0.3)

# 设置图表标题和轴标签
ax.set_title('Distribution of Books by Year', fontsize=16, fontweight='bold')
ax.set_xlabel('Year of publication', fontsize=14)
ax.set_ylabel('The number of books', fontsize=14)

# 设置网格线（可选）
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# 设置x轴刻度标签的旋转角度和字体大小（如果年份很多，可能需要调整）
ax.set_xticks(publication_counts.index)
ax.set_xticklabels(publication_counts.index, rotation=45, fontsize=12)

# 添加图例
ax.legend(loc='upper left', fontsize=12)

# 优化布局（可选）
plt.tight_layout()

# 显示图表
plt.show()