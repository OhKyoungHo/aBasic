# data/sample.json을 읽고 합계를 출력
# 총 ~~입니다 출력

f = open('./data/sample.json', 'rt', encoding='utf-8')
data = f.read()
f.close()

import json
fruit = json.loads(data)
print(fruit)
print(type(fruit))

sum = 0
for k, val in fruit.items():
    print(k, '>', val)
    sum += int(val['count'])*int(val['price'])
print(sum)

