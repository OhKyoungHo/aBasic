import math
import numpy

"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨
    - int() / float() / str() 자료형변환  ( eval() 사용보다는 형변환을 권장 )
"""
from builtins import print

#-------------------------------------------
# 나이를 입력받아 +1을 하여 출력하고 키를 실수형으로 입력받아 출력
#만약 형변환 안하면 문자랑 숫자랑 더해져서 오류 발생
# age = int(input('나이를 입력->'))
# age += 1
# print('나이 : ', age)

# eval을 쓰면 정수를 쓰면 int, 실수값으로 쓰면 float type 출력
# height = eval(input('키를 입력->'))
# print('키 : ', height)
# print(type(height))

#  eval()
print('1+2')    # 1+2
print(eval('1+2'))  # 3

#----------------------------------
# 단을 입력받아 구구단을 구하기
#
# for i in range(10):
#     print(i)

# cal = int(input('원하는 단을 입력'))
# for i in range(10):
# #for i in range(1:9):
#     print(' {0} * {1} = {2}'.format(cal, i, cal*i))




#-----------------------------------------
# print() 함수
print('안녕' + '친구')
print('안녕', '친구')
print('안녕' '친구')

for i in range(5):
    print(i)
# 각 끝나는 부분마다 / 붙이기
for i in range(5):
    print(i, end='/')
print()
# i가 4보다  작을 경우 /를 붙이지 않음
for i in range(5):
    print(i, end='/' if i<4 else "")

print("---------------")

# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
#java  클래스명 문자열1 문자열2
#                [0]     [1]
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0      1      2      3


#----------------------------------
#1번
# num1 = int(input('정수를 입력하세요'))
# num2 = int(input('정수를 입력하세요'))
# num3 = int(input('정수를 입력하세요'))
# num4 = int(input('정수를 입력하세요'))
# num5 = int(input('정수를 입력하세요'))
#
# print(' 평균 : {0}'.format((num1 + num2 + num3 + num4 +num5)/5.0))

#2번
'''
list 타입에서 제공하는 reverse 함수는 list 내의 요소를 역순으로 정렬
입력받은 문자열을 list로 변환시켜주고 reverse 함수를 사용한 후 join 함수를 이용하여  문자열로 변환 후 출력
'''
output = "abcde"
output_list = list(output)
output_list.reverse()
print(''.join(output_list))

#3번

# numbers = input('정수리스트입력:')     #입력값 받아오기
# nums = numbers.split()              #list로 변환
# sum = 0.0                           #총합변수 선언
# for i in range(len(nums)):          #총합 계산
#     sum = sum + float(nums[i])
#
# avg=sum/len(nums)                   #평균수 계산
#
# #표준편차계산(수학문제)
# aa = 0.0
# for i in range(len(nums)):
#     aa = aa + abs(float(nums[i])-avg)**2
# bb = aa/(len(nums)-1)
# bb=math.sqrt(bb)
# print('평균= {}'.format(avg))
# print('표준편차{:.2f}'.format(bb))

# 문자열을 반복문으로 돌리는데 해당 값을 int로 바꿔서 배열로 만들었다
numbers = [int(x) for x in input('정수리스트입력:').split()]
print("평균 :", numpy.mean(numbers))
print("표준편차 {:.2f}".format(numpy.std(numbers)))

# arr = input('정수리스트 입력 : ').split()
# a = int(arr[0])
# b = int(arr[1])
# c = int(arr[2])
# d = int(arr[3])
# e = int(arr[4])
# sum = a+b+c+d+e
# avg = sum / 5
# print('평균 : ', avg)
# bunsan = ( (a-avg)**2 + (b-avg)**2 + (c-avg)**2 + (d-avg)**2 + (e-avg)**2 )/5
# print(bunsan)
# pyuncha = bunsan ** (1/2)
# print('표준편차 : ', pyuncha)

#4번
phonenum =[[],['A','B','C'],['D','E','F'], ['G','H','I'],['J','K','L'],['M','N','O'],
           ['P','Q','R','S'],['T','U','V'], ['W','X','Y','Z']]
output = input('문자열을입력하시오: ')
result = ''
for num in output:
    for i in range(len(phonenum)):
        if num.upper() in phonenum[i]:
            # 1에는 아무 문자가 없기 때문에 1을 더해준다
            # 숫자값끼리 더하면 합한 값이 나오기 때문에 str로 형 변환
            result += str(i+1)
print(result)

