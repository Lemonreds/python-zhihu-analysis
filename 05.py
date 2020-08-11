# encoding=utf-8
import pandas as pd  # 数据处理库
import re  # 正则表达式库
import jieba  # 结巴分词库

from common.parse_json import parse_json
from common.file_help import open_file, write_file

print('---------- 05 地区分布统计图 START ----------')

f = open_file()

ids = [] # 地区对应的id
names = []   # 地区对应的名字

# 逐行读取数据
for line in f:
    d = parse_json(line)# 转成json，转换失败 d 为 -1
    if d != -1:
        locations = d['locations'] # 取 locations ，locations是数组，进行遍历
        for location in locations:
            ids.append(location['id'])
            names.append(location['name'].replace('市','')) # 这里使得 '广州市' === '广州'

# 使用pandas构建表，列为 name id cnt(计数)
corpus = pd.DataFrame({'name': names,'id': ids, 'cnt': 1}, columns=['name','id', 'cnt'])

# 对表进行分组，以name为合并列，总数记录到 cnt 列上
g = corpus.groupby(['name'], as_index=False).agg('cnt').sum().sort_values(
    'cnt', ascending=False).head(100) # head(100） 取100个



data = []
# 将数据转换为字典类型 以写入到文件
for i in g.values:
    temp = {'name': i[0], 'value': i[1]}
    data.append(temp)

f.close()
# 写到 results/05.json 中
write_file('05', data)
print('---------- 05 地区分布统计图 END ----------')
