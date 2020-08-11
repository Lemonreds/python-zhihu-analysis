# encoding=utf-8
import pandas as pd  # 数据处理库
import re  # 正则表达式库
import jieba  # 结巴分词库

from common.parse_json import parse_json
from common.file_help import open_file, write_file

print('---------- 10 专业信息 START ----------')

f = open_file()

names = []  # 专业名称

# 逐行读取数据
for line in f:
    d = parse_json(line)  # 转成json，转换失败 d 为 -1
    if d != -1:
        educations = d['educations']  # 取教育
        for edu in educations:
            try:
                major_name = edu['major']['name']
                if major_name.strip() != '':  #判断非空 才添加该专业
                    names.append(major_name)
            except:
                pass

# 使用pandas构建表，列为 name cnt(计数)
corpus = pd.DataFrame({'name': names, 'cnt': 1}, columns=['name', 'cnt'])

# 对表进行分组，以name为合并列，总数记录到 cnt 列上
# 并获取最大前20条
g = corpus.groupby(['name'], as_index=False).agg('cnt').sum().sort_values(
    'cnt', ascending=False).head(20)

data = []

# 将数据转换为字典类型 以写入到文件
for i in g.values:
    temp = {'name': i[0], 'value': i[1]}
    data.append(temp)

f.close()
# 写到 results/10.json 中
write_file('10', data)
print('---------- 10 专业信息  END ----------')