
# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행

   (3) while 문
        while 조건문 :
            문장들
        else :
            문장들

"""
a = 112                  # 숫자형
b = ['1','2','3']       # 리스트
c = '987'                # 문자열
d = tuple(b)             # 튜플
print(d)
e = dict(k=5, j=6)       # 딕셔너리

for entry in e:     # a(숫자형)는 반복이 안되지만 b부터 e까지는 반복된다.
    print(entry)
# 문자열도 집합으로 취급하여 하나씩 뽑는다


# 딕셔너리인 경우
for entry in e:
    print(entry, e[entry])
else:   # for문은 무언가가 true니까 돌아가는 것 -> true인 동안 출력 -> 끝나면 false
    print('End')

# 1부터 10까지의 합 구하기
'''
int sum = 0;
for (int i = 1; i <= 10; i++) {
    sum += i;
}

for <타겟 변수> in 집합 객체:
    문장들
'''
sum = 0
for i in range(1, 11):  # 1부터 11-1까지를 i라는 변수에 담아라
    sum += i
print('1부터 10까지의 합계: ', sum)

# 1부터 10까지의 홀수의 합 구하기
sum = 0
for i in range(1, 11, 2):  # 1부터 11-1까지를 2씩 건너뛰어 i라는 변수에 담아라
    sum += i
print('1부터 10까지 홀수의 합계: ', sum)


"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""
for i in range(2, 10):  # 2부터 10-1까지를 i라는 변수에 담아라
    print('-'*10, i, '단')
    for j in range(1, 10):
        print(i, '*', j, '=', i*j)


li = ['z', 'x', 'y']
while li:
    data = li.pop()
    print(data)
else:
    print('End')
# li의 요소들을 뒤에서부터 pop하여 li에는 남은 요소가 없게 된다

# 1번
fruit = 'apple'
if fruit == 'Apple':
    fruit = 'Apple'
elif fruit == 'fruit':
    fruit = 'fruit'
else:
    fruit = fruit
print(fruit)

# 2번
number = ["1", 2, 3, float(4), str(5)]
if number[4] == 5:
    print(type(number[0]))
elif number[3] == 4:
    print(number[2:-1])

# 3번
num = 0
i = 1
while i < 8:
    if i % 3 == 0:
        break
    i += 1
    num += i

print(num)

# 4번
result = 0
for i in range(5, -5, -2):
    if i < -3:
        result += 1
    else:
        result -= 1
print(result)

# 5번 986531
num = ""
for i in range(10):
    if i <= 5 and (i % 2)==0:
        continue
    elif i is 7 or i is 10:
        continue
    else:
        num = str(i) + num
print(num)

# 6번 1800원
coupon = 0
money = 20000
coffee = 3500
while money > coffee:
    if coupon < 4:
        money = money - coffee
        coupon += 1
    else:
        money += 2800
        coupon = 0
print(money)

# 6
list_data_a = [1, 2]
list_data_b = [3, 4]
for i in list_data_a:
    for j in list_data_b:
        result = i + j  # 축적이 아닌 마지막 것만 계산하도록 식 설정

print(result)
