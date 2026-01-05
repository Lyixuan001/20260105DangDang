import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

# 1. 读取Excel文件
file_path = 'D:\\Eytalsixone\\wajuedata\\last\\month_good_data.xlsx'  
data = pd.read_excel(file_path)

# 2. 提取书名列
book_titles = data['书名']

# 3. 将所有书名合并成一个长字符串
all_titles_combined = ' '.join(book_titles.astype(str))

# 4. 清洗数据，去除书名中的标点符号和无关字符
# 这里我们使用正则表达式去除非中文字符
cleaned_titles = re.sub(r'[^\u4e00-\u9fa5]+', ' ', all_titles_combined)

# 5. 使用wordcloud库生成词云图
# Windows系统可以使用'simsun.ttc'字体
font_path = 'C:\\Windows\\Fonts\\simsun.ttc'  

wordcloud = WordCloud(
    font_path=font_path,
    width=800, height=400,
    background_color='white'
).generate(cleaned_titles)

# 显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # 不显示坐标轴
plt.show()
# 保存词云图为图片
plt.savefig('D:\\Eytalsixone\\wajuedata\\last\\wordcloud.png', dpi=300, bbox_inches='tight')