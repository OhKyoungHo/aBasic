#주석
from builtins import print

a = 5
print(a)

if a > 4:
    print('5보다 크다')
else:
    print('5보다 작다')

for i in range(10):
    print(i)

# 반복문에서 들여쓰기(4스페이스 = 1탭 )를 해줌으로써 표현
# 한줄은 최대 80자 이내로
# 불필요한 공백은 피함

# PEP8 규칙
# - = 연산자는 1칸 이상 띄우지 않는다
# - 변수명에 소문자 l(엘), 대문자 O(오), 대문자 I (아이)는 금한다
# lIOO = 100 (엘아이오오)
# - 주석은 항상 갱신하고, 불필요한 주석을 지운다
# - 함수명은 소문자로 구성하고 필요하면 밑줄(_)로 나눈다


#파이썬 특징
#읽기 쉬운 언어 BUT, map, zip, reduce 읽기 어려움
#강력한 라이브러리

# 여러줄 주석 방법
"""여러줄 주석"""
'''여러줄 주석'''
# 문자줄이 여러줄인 경우 /n보다 """ ,'''이 더 유용하다
# 문자열 표시(""" 사용시 줄 바꿈이 출력에 그대로 적용됨)
print("헬로우")
print('hello')
print("""안
녕""")
print('''올
라''')

'''
여러줄 
주석인가?????
'''

'''
자바의 변수(기본형, 참조형)
int a = 10;

파이썬의 변수(거의 참조형이다 라고 생각하면 편하다!)
파이썬의 모든 자료형은 객체로 취급한다.
a=7

7 객체을 가리키는 변수 a이다
변수 a는 7이라는 정수형 객체를 가리키는 레퍼런스

자바의 변수와 파이썬의 변수는 다르다

[변수명 규칙]
    - 영문자 + 숫자 + _ 조합
    - 첫글자에 숫자는 안됨
    - 대소문자 구별
    - 길이 제한 없음
    - 예약어 사용 안됨   

'''
# 예약어: 변수명으로 사용할 수 없다
# keyword 모듈을 로딩
import keyword
print(keyword.kwlist)

#7을 가리키는 변수 a
a = 7
#7을 가리키는 변수 b
b = 7
print(type(a))
#  값  <class 'int'> 출력, 파이썬은 그냥 참조형이라 생각하면 편하다

#주소값 확인
print(id(a))
print(id(b))
print(id(7))

'''해당 위의 값은 주소 값이 같음
a,b,7을 가리키는 값은 같다. 즉 각 변수의 객체가 같고, 주소가 같게 나옴을 확인할 수 있다.  
또한 값은 계속 바뀌지만 가리키는 값은 같다'''

'''여러 변수 선언'''
a, b = 5, 10
# python style
print('a+b=', a+b)
# java style(에러발생)
# print('a+b='+(a+b))


# 두 변수의 값 swapping(서로 교환)

'''
자바방식
임시메모리를 만들어서 삼각형 구조로 교환해야 한다()
a=10
b=20
temp=a
a=b
b=temp
'''
# 파이썬 방식
a, b = 10, 20
a, b = b, a
print('A=', a, ", B=", b)

# new <->del(delete)
# 변수 삭제 del
del b
# b를 찾지 못해서 에러 발생
#print('A=', a, ", B=", b)

'''숫자형 종류
- 정수형
- 실수형
- 복소수형 1+2j, 3i(많이 사용안함..)
- 8진수 0o25 21
- 16진수 0x25
 # 파이션의 모든 자료형은 객체로 취급한다

[10진수]
345 = 3*10(2) +4*10(1) +5*10(0)
    = 3*100 + 4*10 + 5*1
[8진수]
25 = 2*8(1) + 5*8(0)
   = 2*8 + 5*1
   = 21
[16진수]
25 = 2*16(1) + 5*16(0)
   = 2*16 + 5*1
   = 37   

[ 기초 연산자 ]
        + : 더하기
        - : 빼기
        * : 곱하기
        / : 나누기(실수값 결과)
        // : 나누기(정수값 결과)
        % : 나머지
        ** : 자승(n제곱)
        2. 관계연산자
        <   >   <=  >=  ==  !=
    
    3. 논리연산자
        not     or      and
        
    4. 이진(비트) 연산자
        ~   :  이진 not   
        |   :  이진 or
        &   :  이진 and
        ^   :  이진 xor
        <<  :  shift
        >>  :  shift
        
    5. 대입연산자
        =
        +=  -=  *=  /=  //= %=
        &=  |=  ^=
        >>= <<=
    
    6. 기타연산자 : 딕셔너리, 문자열, 리스트, 튜플 등의 자료형에서 사용
        in      : 요소에 포함되면 true, 없으면 false
        not in  : 요소에 포함되지 않으면 false, 없으면 true
      

    [참고] 증가(++), 감소(--) 연산자 없음
    [참고] is / not is 사용하지 못하게 에러 발생함               

'''
a = 5
b = 2
print('a + b =', a+b)
print('a - b =', a-b)
print('a * b =', a*b)
print('a / b =', a/b)
print('a // b =', a//b)
print('a % b =', a % b)
print('a ** b =', a**b)

print('H' in 'Hello')  # True
print('H' not in 'Hello')  # False

# 출력 포맷
#{index(순서): format(출력형태)}
# index를 바꾸면 출력값 순서가 바꿀 수 있다
y = 8.3/2.7
z = 8.3//2.7
print(y, '/', z)  # 3.074074074074074 / 3.0
print('실수 1 : {}, 정수 1 : {}'.format(y, z))
print('실수 1 : {0}, 정수 1 : {1}'.format(y, z))
print('실수 1 : {1}, 정수 1 : {0}'.format(y, z))
print('실수 1 : {0:0.1f}, 정수 1 : {0}'.format(y, z))  #소수점 1자리까지만 나옴


#연습문제
#1번 True
a = 777
b = 777
print(a == b)
# 2번 : 1번
# 3번  12.25 0.0 1.75 0.0
a = 3.5
b = int(3.5)
print(b)  # 3
print(a**((a // b) * 2))
#  12.25
print(((a - b) * a) // b)
#  0.0
b = (((a - b) * a) % b)
print(b)
#  1.75
print((a * 4) % (b * 4))
#  0.0

#4번 4번

#5번 2번

#6번 3번
a = 10.6
b = 10.5
print(a * b)
print(type(a + b))

#7번 2번
a = "3.5"
b = 4
print(a * b)

#8번 2번
a = "3.5"
b = "1.5"
print(a + b)

#9번 3번
a = '3'
b = float(a)
print(b ** int(a))

#10번 3번
# 변수에 할당된 값은 메모리 공간에 저장

#11번 5번
a = '20'
b = '4'
#  print(type(float(a / b)))
#  str타입과 str타입이므로 나눌 수 없다. +기호인 경우 붙어서 작성할 수 있다.

#12번 5번
'''
변수 이름에는 다음 문자만 사용 가능합니다: 
소문자(a - z), 대문자(A - Z), 숫자(0 - 9), 언더바(_)
변수명은 대소문자를 구분합니다: apple, Apple, aPPle는 모두 다른 변수
변수명은 숫자로 시작할 수 없습니다. 소문자, 대문자, 언더바로만 시작할 수 있습니다.
예약어는 변수명으로 사용할 수 없습니다.

'''

#문자열 연습
'''문자열을 ""이나 ''으로 표현

문자열 연산
     ※ 문자열 합치기 : 문자열 + 문자열
     ※ 문자열 반복 : 문자열 * 숫자

'''
msg ='안녕 파이썬'

print(msg)

msg = """
    안녕하세요.
    저는 성이 파이이고,
    이름은 썬입니다.
    잘 부탁합니다.
"""
print(msg)

msg = '''
    행복합시다
    즐깁시다
    오늘도
'''
print(msg)

print('-'*50)
print(a+b)


a = '독도는 '
b = "한국이다. "
print('-'*50)
print(a + b)
print('ox'*25)
print((a + b)*3)
print('='*50)

# ****************************
# 주의 : 문자열 + 숫자 => 에러발생
a = '독도'
d = a + str(100)
print(d)

# 인덱스는 0부터 시작한다
# s[i] : s 문자열에서 i번째 문자 추출
# s[i:j] : s 문자열에서 i번째에서 j-1까지의 문자 추출
# s[i:j:k] : s 문자열에서 i번째에서 j-1까지에서 k개씩 건너뛰어 문자 추출
# s[-i] : s 문자열에서 뒤에서부터 i번째 문자 추출( 뒤에서 인덱스는 1부터 센다 ) ★★★★★


msg = '오늘도 행복도 하다'
print(msg[0])
print(msg[0:2])
print(msg[1:6])
print(msg[0] + msg[2] + msg[4])
print(msg[0:6:2])
print(msg[9])

msg = '오늘도 행복도 하다'
#2번에서 5번째 전까지
print(msg[2:5])
#2번부터
print(msg[2:])
#5번째 전의 문자까지
print(msg[:5])
#문자열 전체
print(msg[:])

# 5번째부터
print(msg[5:])
# 5번째 전의 문자까지
print(msg[:5])
# 5번째  전의 문자까지에서 2개씩 건너뛰어
print(msg[0:5:2])
# 문자열 전체에서 2개씩 건너뛰어
print(msg[::2])

"""
 날짜와 시간을 표현하는 문자열에서 '2020-02-22 : 12:05:12'
    '2020년 2월 22일' 출력
    '12시 5분' 출력
"""

msg = '2020-02-22 : 12:05:12'
# 월(달)
print(msg[5:7])
# 분
print(msg[16:18])

print(msg[0:4] + '년' + msg[5:7] + '월' + msg[8:10]+'일')
print(msg[13:15]+'시' + msg[16:18]+'분')
print(msg[-8:-6]+'시' + msg[-5:-3]+'분')

# [과제] 회문 : 거꾸로 배열해도 같은 단어 혹은 문장이 되는 것
# 입력받은 문자열이 회문인지 아닌지 구별
# 주어진 단어가 회문인지 판별하는 함수 palindrome()을 작성
s = '12021'
s1 = s[::-1]
print(s,s1)

'''
#       s.count('글') : s 문자열에서 '글'이라는 문자 개수 세기
#       s.index('글') : s 문자열에서 문자 '글' 위치 알려주기
#       s.find('글') : s 문자열에서 문자 '글' 위치 알려주기
#       s.rfind('글') : s 문자열에서 문자 '글' 오른쪽에서 왼쪽으로 찾아서 위치 알려주기
#       len(s) : s 문자열 길이
'''
msg ="오늘도 행복도 하다"
print(msg.index('행복'))  # 4
print(msg.find('행복'))   # 4
# print(msg.index('가자')) # 에러발생
print(msg.find('가자'))  # -1
print(msg.rfind('행복'))  # 4
print(len(msg)) # 10
print(msg.count('도'))   # 2


#   s.upper() : 소문자를 대문자로
#   s.lower() : 대문자를 소문자로
#   s.lstrip() : 왼쪽 공백 지우기
#   s.rstrip() : 오른쪽 공백 지우기
#   s.strip() : 양쪽 공백 지우기

msg = '  This is My Life     '
print(msg.upper())
print(msg)
print(msg.strip())
#  중간 공백 없앨려면??
print(msg.replace(" ", ""))


#   s.replace("a","b")  :  s 문자열에서 단어 a를 단어 b로 바꾸기
#   s.split() : s 문자열을 공백으로 나누기
#   s.split('z') : s 문자열을 z 기호로 나누기
#   d.join(s) : d 단어를 s 문자열에 삽입 ★★★★★

