# encoding=utf-8
import pandas as pd  # 数据处理库
import re  # 正则表达式库
import jieba  # 结巴分词库

from common.parse_json import parse_json
from common.file_help import open_file, write_file

print('---------- 07 职业信息 START ----------')

f = open_file()

ids = [] # 职业id
names = [] # 职业名

# 逐行读取数据
for line in f:
    d = parse_json(line) # 转成json，转换失败 d 为 -1
    if d != -1:
        employments = d['employments'] # 取 employments  
        for emp in employments: # 遍历 employments
            try:
                job_id = emp['job']['id'] # 取到职业id
                job_name = emp['job']['name'] # 取到职业name
                if job_name.strip() != '':# 判断非空才添加
                    ids.append(job_id)
                    names.append(job_name)
            except :
                pass
            
            
 # 使用pandas构建表，列为 name id cnt(计数)
corpus = pd.DataFrame({'name': names,'id': ids, 'cnt': 1}, columns=['name','id', 'cnt'])

# 对表进行分组，以name为合并列，总数记录到 cnt 列上
g = corpus.groupby(['name','id'], as_index=False).agg('cnt').sum().sort_values(
    'cnt', ascending=False).head(100)



data = []

# 将数据转换为字典类型 以写入到文件
for i in g.values:
    temp = {'name': i[0],'id': i[1],'value': i[2]}
    data.append(temp)

f.close()
# 写到 results/07.json 中
write_file('07', data)
print('---------- 07 职业信息 END ----------')
