# 匯入需要的模組
import os
import sys
import pandas as pd
from bs4 import BeautifulSoup

# 讀取bug5編碼用
import codecs

path = '/Users/hazel_lin/Documents/Lin Yi-Sin/實習或工作/COVID-19 project/Data/0111data/高速公路計程收費通行量.html'

# 空list等下放資料
data = []

# 從html的header找table（表格）的資料
list_header = []
fr = codecs.open(path, 'r', encoding='big5', errors='ignore')
soup = BeautifulSoup(fr, 'html.parser')
header = soup.find_all("table")[1].find("tr")

for items in header:
    try:
        list_header.append(items.get_text())
    except:
        continue

# 用BeautifulSoup來爬html裡面的table裡面的資料
HTML_data = soup.find_all("table")[1].find_all("tr")[1:]

for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue
    data.append(sub_data)

# 如果噴error像是column的數量不符的話，先把list裡面的東西印出來測試
# print(list_header)
# print(sub_data)

# 把list的資料存到Pandas的DataFrame
dataframe = pd.DataFrame(data = data, columns = list_header)
# print(dataframe)

# 把DataFrame匯出成csv，編碼用utf-8
dataframe.to_csv('高速公路計程收費通行量.csv', encoding='utf-8')