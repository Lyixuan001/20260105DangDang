# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 09:36:04 2024

@author: 28154
"""
# 导入所需的库
import requests  # 用于发送HTTP请求
from lxml import etree  # 用于解析HTML和XML文档
import pandas as pd  # 用于数据处理和分析

# 设置请求头，模拟浏览器访问
headers = {
    "User-Agent": "xxxsh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

# 定义函数，用于获取当当网的图书信息
def get_dangdang_info(url, month):
    # 发送HTTP GET请求获取网页内容
    html = requests.get(url, headers=headers)
    # 设置正确的编码，以避免乱码
    html.encoding = html.apparent_encoding
    # 使用lxml的etree解析HTML文档
    selector = etree.HTML(html.text)
    # 通过XPath查询获取包含图书信息的div元素列表
    datas = selector.xpath('//div[@class="bang_list_box"]')
    # print(datas)
    # 初始化一个空列表，用于存储图书信息
    book_info = []
    # 遍历每个包含图书信息的div元素
    for data in datas:
        # 提取排名信息
        Ranks = data.xpath('ul/li/div[1]/text()')
        # 提取书名链接中的文本（书名）
        names = data.xpath('ul/li/div[3]/a/text()')
        # 提取评论链接中的文本（评论数）
        pingluns = data.xpath('ul/li/div[4]/a/text()')
        # 提取作者链接中的文本（作者）
        authors = data.xpath('ul/li/div[5]/a/text()')
        # 提取出版社信息
        chubans = data.xpath('ul/li/div[6]/span/text()')
        # 提取价格信息
        jiages = data.xpath('ul/li/div[7]/p[1]/span[1]/text()')
        # 提取原价信息
        yuanjias = data.xpath('ul/li/div[7]/p[1]/span[2]/text()')
        # 提取折扣信息
        discounts = data.xpath('ul/li/div[7]/p[1]/span[3]/text()')
        # 提取书名链接的URL
        urls = data.xpath('ul/li/div[3]/a/@href')
        # 使用zip函数同时遍历上述所有列表，并组装成包含所有图书信息的列表
        for Rank, url, name, pinglun, author, chuban, jiage, yuanjia, discount in zip(Ranks, urls, names, pingluns, authors, chubans, jiages, yuanjias, discounts):
            book_info.append([month, Rank, url, name, pinglun, author, chuban, jiage, yuanjia, discount])
    # 返回包含所有图书信息的列表
    return book_info

# 主程序入口
if __name__ == '__main__':
    # 初始化一个空列表，用于存储近四年的图书数据
    book_data = []
    # 遍历1-11月
    for i in range(1,12):  
        # 遍历每一页（1到25页，当当网的分页通常是每页显示一定数量的图书）
        for j in range(1, 26):  
            url = f'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-month-2024-{i}-1-{j}'
            print(url)  # 打印URL
            # 调用函数获取当前页面的图书信息，并添加到book_data列表中
            book_data += get_dangdang_info(url, i)
    # 使用pandas的DataFrame创建一个新的DataFrame对象，用于存储图书数据
    df = pd.DataFrame(book_data, columns=['月份', '排名', '链接', '书名', '评论数', '作者', '出版年份', '价格', '原价', '折扣'])
    # 将DataFrame对象保存为Excel文件
    df.to_excel('month1-11.xlsx', index=False)
    # 打印提示信息，告知用户数据已保存
    print("2024年month1-11数据已保存")