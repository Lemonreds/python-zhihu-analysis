# encoding=utf-8

from common.parse_json import parse_json
from common.file_help import open_file, write_file

print('---------- 01 用户性别分布图 START ----------')

f = open_file()

# 统计结果的初始值
data_gender = [{
    'name': '男性',
    'value': 0
}, {
    'name': '女性',
    'value': 0
}, {
    'name': '其他',
    'value': 0
}]

# 逐行读取数据
for line in f:
    d = parse_json(line) # 转成json，转换失败 d 为 -1
    if d != -1:
        gender = d['gender']
        if gender == 1:
            data_gender[0]['value'] += 1
            pass
        elif gender == 0:
            data_gender[1]['value'] += 1
            pass
        else:
            data_gender[2]['value'] += 1
            pass

f.close()

# 写到 results/01.json 中
write_file('01', data_gender)
print('---------- 01 用户性别分布图 END ----------')
