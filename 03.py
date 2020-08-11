# encoding=utf-8
import pandas as pd  # 数据处理库
import re  # 正则表达式库
import jieba  # 结巴分词库

from common.parse_json import parse_json
from common.file_help import open_file, write_file

print('---------- 03 个人描述词云图 START ----------')

f = open_file()

words = []  # 所有数据的 description 字段分词后的集合
cnreg = "[\u4e00-\u9fa5]+"  # 中文正则表达式

# 逐行读取数据
for line in f:
    d = parse_json(line)  # 转成json，转换失败 d 为 -1
    if d != -1:
        seg_list = jieba.cut(d['description'])  # 使用jieba库进行分词
        for word in seg_list:
            if re.match(cnreg, word):  # 判断是中文，才存到words
                words.append(word)

# 使用pandas构建表，列为 word cnt(计数)
corpus = pd.DataFrame({'word': words, 'cnt': 1}, columns=['word', 'cnt'])

# 对表进行分组，以word为合并列，总数记录到 cnt 列上
g = corpus.groupby('word', as_index=False).agg('cnt').sum().sort_values(
    'cnt', ascending=False).head(100)  # head(100） 取100个

data = []
# 将数据转换为字典类型 以写入到文件
for i in g.values:
    temp = {'name': i[0], 'value': i[1]}
    data.append(temp)

f.close()
# 写到 results/03.json 中
write_file('03', data)
print('---------- 03 个人描述词云图 END ----------')
