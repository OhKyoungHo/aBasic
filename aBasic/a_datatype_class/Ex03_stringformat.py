
# -----------------------------------------
#  문자열 포맷
#       0- 문자열 포맷팅
#               print('내가 좋아하는 숫자는 ', 100 )
#       1- format() 이용
#               print('내가 좋아하는 숫자는 {0:d} 이다'.format(100) )
#       2- % 사용
#               print('내가 좋아하는 숫자는 %d 이다' % 100 )
#       성능(속도)는 %이 더 빠르다고는 하지만 코드가 깔끔하게 하는 것이 더 중요하다고 하고는
#       어느 것으로 선택하라고는 안 나옴


# format()이용


# [참고] http://pyformat.info

# % 이용 - printf() 역할
name = '홍길동'
age = 22
height = 170.456

print('이름 :{0}, 나이 :{1}, 키:{2:.1f}'.format(name, age, height))

print('이름 : %s, 나이 : %d, 키 : %.1f' % (name, age, height))

#--------------------------------------------------
# 실수인 경우
#1. 답 3번
a = 11

b = 9

print('a' + 'b')

#2번 21

fact = "Python is funny"

print(fact.count('n'))
print(fact.find('n'))
print(fact.rfind('n'))
print(str(fact.count('n') + fact.find('n') + fact.rfind('n')))
#3번 1 gachon Human

text = 'Gachon CS50 - programming with python'

text2 = "Human cs50 knowledge belongs to the world "

text.lower()
text = 'gachon cs50 - programming with python'
print(text[:5] + text[-1] + text[6] + text2.split()[0])
#  gachon, n, " ",  Human

#  4번 introduction programming with python 2번
class_name = 'introduction programming with python'

for i in class_name:

    if i == 'python':
        i = i.upper()

print(class_name)

#  5번 1010102

a = '10'

b = '5-2'.split('-')[1]

print(a * 3 + b)

#6번 aa

a = "abcd e f g"
b = a.split()
print(b)
c = (a[:3][0])
print(c)
d = (b[:3][0][0])
print(d)
print(c + d)

#7번 8,1
result = "CODE2018"

print("{0},{1}".format(result[-1], result[-2]))

#8번 3번
'''capitalize( ):  첫번째만 대문자 나머지는 소문자로
   title() : 문자열 내 띄어쓰기 기준으로 각 단어의 첫글자는 대문자로, 나머지는 소문자로 변환한다.
   strip() :  문자열 양 끝에 있는 공백을 제거해주고, 공백을 제거한 새로운 문자열을 반환
   isdigit() : 문자열이 '숫자'로만 이루어져있는지 확인하는 함수 
'''