import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# 读取Excel文件
file_path = 'D:\\Eytalsixone\\wajuedata\\last\\month_good_data.xlsx'
data = pd.read_excel(file_path)

# 数据预处理
def convert_discount_to_float(discount_str):
    if isinstance(discount_str, str):
        # 使用正则表达式提取数值部分
        match = re.match(r'(\d+\.\d+)', discount_str)
        if match:
            return float(match.group(1))
        else:
            return None
    else:
        return discount_str

# 应用转换函数


# # 1. 每个月份的平均折扣情况
# monthly_discounts = data.groupby('月份')['折扣'].mean()

# # 创建图表
# plt.figure(figsize=(10, 6))
# sns.set(style="whitegrid")  # 设置Seaborn的风格
# sns.lineplot(x=monthly_discounts.index, y=monthly_discounts.values, marker='o', color='blue', linewidth=2.5, markersize=10)

# # 添加数据标签
# for x, y in zip(monthly_discounts.index, monthly_discounts.values):
#     plt.text(x, y, f'{y:.2f}', ha='center', va='bottom', fontsize=10, color='red')

# # 设置标题和轴标签
# plt.title('The average monthly discount rate', fontsize=16, fontweight='bold')
# plt.xlabel('month', fontsize=14)
# plt.ylabel('Average Discount', fontsize=14)

# # 调整轴标签的字体大小
# plt.xticks(monthly_discounts.index, fontsize=12)
# plt.yticks(fontsize=12)

# # 添加网格线
# plt.grid(True, linestyle='--', alpha=0.7)

# # 保存图表为图片文件
# plt.savefig('D:\\Eytalsixone\\wajuedata\\last\\monthly_discount_average.png', dpi=300)  # 可以指定分辨率，如dpi=300
 
# # 显示图表
# plt.show()

# 3. 不同出版年份的平均折扣情况
# yearly_discounts = data.groupby('出版年份')['折扣'].mean()
# plt.figure(figsize=(10, 6))
# sns.lineplot(x=yearly_discounts.index, y=yearly_discounts.values, marker='o')
# plt.title('不同出版年份的平均折扣情况')
# plt.xlabel('出版年份')
# plt.ylabel('平均折扣')
# plt.xticks(rotation=45)  # 确保年份标签正确显示
# plt.show()
 # 计算每个出版年份的折扣总和
# 筛选2005-2025年的数据
# 确保出版年份是正确的日期类型
# 确保出版年份是正确的日期类型
data['折扣'] = data['折扣'].apply(convert_discount_to_float)

# 确保其他列的数据类型正确
data['价格'] = data['价格'].astype(float)
data['原价'] = data['原价'].astype(float)

# 确保出版年份是正确的日期类型
data['出版年份'] = pd.to_datetime(data['出版年份'])

# 提取年份并转换为整数类型
data['出版年份'] = data['出版年份'].dt.year

# 筛选2005-2025年的数据
data = data[(data['出版年份'] >= 2005) & (data['出版年份'] <= 2025)]

# 计算每个出版年份的平均折扣
yearly_discounts = data.groupby('出版年份')['折扣'].mean()

# 将平均折扣越大，y值越小
yearly_discounts_inverted = 10 - yearly_discounts

# 设置支持中文的字体
plt.rcParams['font.sans-serif'] = ['simsun']  # 使用'simsun'字体名称
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 创建图表
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")  # 设置Seaborn的风格

# 绘制折线图
sns.lineplot(x=yearly_discounts_inverted.index, y=yearly_discounts_inverted.values, marker='o', color='blue', linewidth=2.5, markersize=10)

# 添加数据标签
for x, y in zip(yearly_discounts_inverted.index, yearly_discounts_inverted.values):
    plt.text(x, y, f'{y:.2f}', ha='center', va='bottom', fontsize=10, color='red')

# 设置标题和轴标签
plt.title('The average discount for each publication year from 2005 to 2025', fontsize=16, fontweight='bold')
plt.xlabel('Year of publication', fontsize=14)
plt.ylabel('10- Average discount', fontsize=14)

# 调整轴标签的字体大小
plt.xticks(fontsize=12, rotation=45)
plt.yticks(fontsize=12)

# 添加网格线
plt.grid(True, linestyle='--', alpha=0.7)

# 自动调整子图参数，使之填充整个图像区域
plt.tight_layout()

# 显示图表
plt.show()
plt.savefig('D:\\Eytalsixone\\wajuedata\\last\\年平均打折.png', dpi=300, bbox_inches='tight')

# 显示图表
# # 4. 不同评论数区间的平均折扣情况
# data['评论数区间'] = pd.cut(data['评论数'], bins=[0, 10000, 50000, 100000, 500000, 1000000, float('inf')], 
#                         labels=['0-10k', '10k-50k', '50k-100k', '100k-500k', '500k-1m', '>1m'])
# comment_discounts = data.groupby('评论数区间')['折扣'].mean()
# plt.figure(figsize=(10, 6))
# sns.barplot(x=comment_discounts.index, y=comment_discounts.values)
# plt.title('不同评论数区间的平均折扣情况')
# plt.xlabel('评论数区间')
# plt.ylabel('平均折扣')
# plt.show()