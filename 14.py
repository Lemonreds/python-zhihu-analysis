# encoding=utf-8
import pandas as pd  # 数据处理库
import re  # 正则表达式库
import jieba  # 结巴分词库
import copy

from common.parse_json import parse_json
from common.file_help import open_file, write_file

print('---------- 14 用户分布内容质量维度分析 START ----------')

f = open_file()
# 初始的 内容质量 区间
counts = [{
    'name': '0-100',# 展示文案
    'value': 0,# 个数统计
    'limit': 100# limit 用于判断是否是该区间
}, {
    'name': '101-1000',
    'value': 0,
    'limit': 1000
}, {
    'name': '1001-1w',
    'value': 0,
    'limit': 10000
}, {
    'name': '1w-10w',
    'value': 0,
    'limit': 100000
}, {
    'name': '10w-100w',
    'value': 0,
    'limit': 1000000
}, {
    'name': '100w+',
    'value': 0,
    'limit': -1
}]

# 三类的初始区间
maping = [{
    'name': '获得收藏数',
    'key': 'favorited_count',
    'values': copy.deepcopy(counts)  # 使用深拷贝，避免引用同一份 counts
}, {
    'name': '获得感谢数',
    'key': 'thanked_count',
    'values':copy.deepcopy(counts)  
}, {
    'name': '获得投票数',
    'key': 'voteup_count',
    'values':copy.deepcopy(counts)  
}]

# 逐行读取数据
for line in f:
    d = parse_json(line)# 转成json，转换失败 d 为 -1
    if d != -1:
        for t in maping: # 三类循环处理
            count = t['values']
            key = t['key']# 当前类的key拼写
            _v = d[key]# 当前类的值 
            for i in count:
                limit = i['limit']
                if _v < limit or limit == -1 :
                    i['value'] +=1
                    break

f.close()
# 写到 results/14.json 中
write_file('14', maping)
print('---------- 14 用户分布内容质量维度分析 END ----------')
