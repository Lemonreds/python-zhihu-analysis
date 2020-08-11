# encoding=utf-8
import json  # json 处理库


#  @desc 将入参 string 转换为 json 后返回
#  @return 成功则返回 json ，失败返回 -1
def parse_json(string):
    result = ''
    inputJson = string.strip()
    if inputJson[len(inputJson) - 1] == ',':
        inputJson = inputJson[:-1]
    try:
        result = json.loads(inputJson)
    except:
        return -1
    return result
