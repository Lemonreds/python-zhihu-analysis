# encoding=utf-8

from common.parse_json import parse_json
from common.file_help import open_file, write_file

print('---------- 02 用户类型分布图 START ----------')

f = open_file()

# 统计结果的初始值
data_user_type = [{
    'name': '个人',
    'value': 0
}, {
    'name': '组织',
    'value': 0
}]

# 逐行读取数据
for line in f:
    d = parse_json(line)  # 转成json，转换失败 d 为 -1
    if d != -1:
        user_type = d['user_type']
        if user_type == 'people':
            data_user_type[0]['value'] += 1
            pass
        elif user_type == 'organization':
            data_user_type[1]['value'] += 1
            pass


f.close()
# 写到 results/02.json 中
write_file('02', data_user_type)
print('---------- 02 用户类型分布图 END ----------')
