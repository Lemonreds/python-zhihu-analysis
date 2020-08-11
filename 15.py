# encoding=utf-8
import pandas as pd  # 数据处理库
import re  # 正则表达式库
import jieba  # 结巴分词库

from common.parse_json import parse_json
from common.file_help import open_file, write_file

print('---------- 15 粉丝数目TOP150用户 START ----------')

f = open_file()

counts = [] # 粉丝数量
names = [] # 名字

# 逐行读取数据
for line in f:
    d = parse_json(line)# 转成json，转换失败 d 为 -1
    if d != -1:
        count = d['follower_count']
        name = d['name']
        counts.append(count)
        names.append(name)

# 使用pandas构建表，列为 name cnt(计数)
corpus = pd.DataFrame({'name': names, 'cnt': counts}, columns=['name', 'cnt'])

# 对表进行排序，取前100个数据
g = corpus.sort_values('cnt', ascending=False).head(100)

data = []

# 将数据转换为字典类型 以写入到文件
for i in g.values:
    temp = {'name': i[0], 'value': i[1]}
    data.append(temp)

f.close()

# 写到 results/15.json 中
write_file('15', data)
print('---------- 15 粉丝数目TOP100用户  END ----------')