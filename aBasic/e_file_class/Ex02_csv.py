# csv 파일 -> 엑셀에서 열림 + 일반 에디터에서 열림
# Common String Value

'''
※ 확장자명을 csv로 만들어두면 엑셀에서 읽을 수 있고, 다양한 작업이 가능하다.
단, 매우 큰 용량의 경우 엑셀로 처리가 불가능하기 때문에 이 경우에는 파이썬 등 다른 방법을 사용해야 한다.
※ csv : common string value 로 평범한 문자열의 데이터를 저장하는 형식
'''

data = [[1, '김', '재동'], [2, '민', '경주'], [3, '전', '병욱']]

# csv 로 파일을 읽고 쓰기 위해서는 패키지를 import 해야 한다.
import csv
# 엑셀은 ANSI 코드로 디코딩해야 하므로  encoding='utf-8-sig' 라고 작성한다.
with open('./data/imsi.csv', 'wt', encoding='utf-8-sig') as f:
    # f.write(data)
    #  writer( ) : 데이터를 저장하기 위한 가상 통로를 얻어온다.
    cout = csv.writer(f)
    # writerow( ) : 데이터를 한 줄식 보낸다.
    cout.writerows(data)

result = []
with open('./data/imsi.csv', 'rt', encoding='utf-8-sig') as g:
    cin = csv.reader(g)
    # 컴프리션에 해당 조건(if hum, []안에 hum이 있는 경우에만 출력)을 넣어줘야 '[]' 없이 출력된다
    result = [hum for hum in cin if hum]
print(result)
