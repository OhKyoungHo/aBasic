f = open('./data/temp.json', 'rt', encoding='utf-8')
data = f.read()
f.close()

print(data)
print(type(data))

import json
# 읽어온 데이터가 json 구조를 가질 수 있도록 json.loads( ) 함수를 처리
# 출력결과는 딕셔너리 타입
hum = json.loads(data)
print(hum)
print(type(hum))

for k, val in hum.items():
    print(k, '>', val)
    print(k,'>>', val['Job'])