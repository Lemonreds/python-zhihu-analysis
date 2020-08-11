import codecs  # 编码辅助库 为了处理写文件乱码问题
import json  # json 处理库

#
# 文件统一工具
#


# @desc 读取 data.json 文件
# @return 文件句柄
def open_file():
    f = codecs.open('datas/data.json', "r", "utf-8")
    return f


# @desc 将data以json格式写到results/下，命名为filename
# @param filename  string
# @param data  json
def write_file(filename, data):
    with codecs.open("results/" + filename + '.json', "w", "utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
