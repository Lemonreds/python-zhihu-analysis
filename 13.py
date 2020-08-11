# encoding=utf-8
import pandas as pd  # 数据处理库
import re  # 正则表达式库
import jieba  # 结巴分词库

from common.parse_json import parse_json
from common.file_help import open_file, write_file

print('---------- 13 回答数和获赞数的关联情况 START ----------')

f = open_file()

# 初始的关联情况区间
counts = [{
    'name': '有回答，有赞同',
    'value': 0,
}, {
    'name': '有回答，无赞同',
    'value': 0,
}, {
    'name': '无回答，无赞同',
    'value': 0,
} ]

# 逐行读取数据
for line in f:
    d = parse_json(line)# 转成json，转换失败 d 为 -1
    if d != -1:
        answer_count = d['answer_count']# 取 answer_count 
        voteup_count = d['voteup_count']# 取 voteup_count 
        if answer_count > 0 and voteup_count > 0:
            counts[0]['value'] +=1
        elif answer_count > 0 and voteup_count == 0:
            counts[1]['value'] +=1
        elif answer_count == 0 and voteup_count == 0:
            counts[2]['value'] +=1            
        

f.close()
# 写到 results/13.json 中
write_file('13', counts)
print('---------- 13 回答数和获赞数的关联情况 END ----------')
