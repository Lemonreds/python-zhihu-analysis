import os


# 所有15个执行py脚本的前缀
names = [
    '01',
    '02',
    '03',
    '04',
    '05',
    '06',
    '07',
    '08',
    '09',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
]

# 串行处理执行每个脚本
for name in names:
    os.system("python " + name + '.py')