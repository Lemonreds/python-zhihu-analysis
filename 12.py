# encoding=utf-8
import pandas as pd  # 数据处理库
import re  # 正则表达式库
import jieba  # 结巴分词库

from common.parse_json import parse_json
from common.file_help import open_file, write_file

print('---------- 12 创建文章数 START ----------')

f = open_file()

# 初始的创建文章数区间
counts = [{
    'name': '0', # 展示文案
    'value': 0,# 个数统计
    'limit': 0# limit 用于判断是否是该区间
}, {
    'name': '1-50',
    'value': 0,
    'limit': 50
}, {
    'name': '51-200',
    'value': 0,
    'limit': 200
}, {
    'name': '201-500',
    'value': 0,
    'limit': 500
}, {
    'name': '501-1000',
    'value': 0,
    'limit': 1000
}, {
    'name': '1000+',
    'value': 0,
    'limit': -1
}]

# 逐行读取数据
for line in f:
    d = parse_json(line)# 转成json，转换失败 d 为 -1
    if d != -1:
        answer_count = d['articles_count'] # 取 articles_count 
        for i in counts:# 进行遍历 判断该值与limit的比较关系
            limit = i['limit']
            if answer_count <= limit or limit == -1:
                i['value'] += 1
                break

f.close()
write_file('12', counts)
print('---------- 12 创建文章数 END ----------')
