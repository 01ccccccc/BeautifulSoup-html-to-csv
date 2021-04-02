import pandas as pd
import csv
import numpy as np

df = pd.read_csv('公共運輸總量增減率.csv', index_col=0)
def tidy_up(x):
    x = str(x)
    x = x.replace(' ', '')
    # x = x.replace(',', '')
    x = float(x)
    return x

# df['汽車客運'] = df['汽車客運'].apply(tidy_up)
df['市區客運'] = df['市區客運'].apply(tidy_up)
df['公路客運'] = df['公路客運'].apply(tidy_up)
df['鐵路客運'] = df['鐵路客運'].apply(tidy_up)
df['臺鐵'] = df['臺鐵'].apply(tidy_up)
df['高鐵'] = df['高鐵'].apply(tidy_up)
df['臺北捷運'] = df['臺北捷運'].apply(tidy_up)
df['高雄捷運'] = df['高雄捷運'].apply(tidy_up)
df['桃園機場捷運'] = df['桃園機場捷運'].apply(tidy_up)
df['新北捷運'] = df['新北捷運'].apply(tidy_up)
df['水上客運'] = df['水上客運'].apply(tidy_up)
df['國內航空'] = df['國內航空'].apply(tidy_up)

df.to_csv('公共運輸總量增減率.csv', encoding='utf8')