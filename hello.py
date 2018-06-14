# -*- coding: utf-8 -*-


#这是一个测试
print("I'm a learner")
print("Hello world")
print(u'你好')

import json
data = [{'id': ' 002', 'name': ' 小明', 'type': ' Grass', 'typeTwo': ' Poison'}]
# 首先要用utf-8的格式打开文件
with open('sty.json', 'w', encoding='utf-8') as f:
    # 然后需要让ensure_ascii设置为False，则可以将中文以utf-8的格式写入
    json.dump(data, f, ensure_ascii=False)
print(data)
