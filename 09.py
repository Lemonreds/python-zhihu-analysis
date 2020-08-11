# encoding=utf-8
import pandas as pd  # 数据处理库
import re  # 正则表达式库
import jieba  # 结巴分词库

from common.parse_json import parse_json
from common.file_help import open_file, write_file

print('---------- 09 学校信息 START ----------')

f = open_file()

names = [] # 学校名字
genders = [] # 性别

# 逐行读取数据
for line in f:
    d = parse_json(line) # 转成json，转换失败 d 为 -1 
    if d != -1:
        gender = d['gender'] # 取性别 
        educations = d['educations']# 取教育
        for edu in educations: # 遍历教育
            try:
                edu_name = edu['school']['name']
                names.append(edu_name)
                genders.append(gender)
            except: # 可能某条数据不存在该字段，会取值错误，这里直接跳过处理
                pass

# 使用pandas构建表，列为 name gender cnt(计数)
corpus = pd.DataFrame({
    'name': names,
    'gender': genders,
    'cnt': 1
},
                      columns=['name', 'gender', 'cnt'])

# 对表进行分组，以name为合并列，总数记录到 cnt 列上
# 并获取最大前10条学校数据
g10 = corpus.groupby(['name'], as_index=False).agg('cnt').sum().sort_values(
    'cnt', ascending=False).head(10)

#最大前10条学校数据
school10 = []

# 将数据转换为字典类型
for i in g10.values:
    name = i[0]
    count = i[1]
    school10.append({
        'name': name,
        'male': 0,
        'female': 0,
        'other': 0,
        'total': count
    })

# 在 arr 中寻找 name 为 _name 的子项
# 找不到 返回 -1
def find(arr, _name):
    for i in arr:
        __name = i['name']
        if __name == _name:
            return i
    return -1

# 开始遍历性别
# 为前10个学校计算 男 女 其他 三个性别的人数
for i in corpus.values:
    name = i[0]
    gender = i[1]
    match = find(school10, name)# 找到的对应学校
    if match != -1:# 找不到对应的学校 不进行处理，非前10学校
        if gender == 1:
            match['male'] += 1
        elif gender == 0:
            match['female'] += 1
        else:
            match['other'] += 1

f.close()
write_file('09', school10)
print('---------- 09 学校信息 END ----------')
