"""
    [ 함수 ]

     - 반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다
     - 역할별 구문을 작성한다

     def 함수명(매개변수):
        수행할 문장들
"""

#함수 만드는 이유 : 역할별로 구분짓기 위해서, 반복적 구문

# (0) 인자도 리턴값도 없는 함수 : 리턴값이 없어서  None이라고 출력
def func():
    print('inside func')
func()  # inside func
result = func()
print(result)       # None

def func():
    print('inside func')
    return 'ok'
func()
result = func()
print(result)

# (1) 리턴값이 있는 함수
def func(arg):
    return arg+5
result = func(10)
print(result)   # 15

# (1) -1 리턴값이 여러개 있는 함수
def func(arg):
    return arg+5, arg-5, arg*5
result = func(10)
print(result)   # (15, 5, 50)   리턴값은 turple 구조로 출력
a, b, c = func(10)
print(a, b, c)   # 15 5 50

# (2) 위치인자 (positional argument) : 인자가 순서대로 들어간다.
def func(greeting, name):
    print(greeting, '!!!!',  name, '님')
func('하이', '박길동')       # 하이 !!!! 박길동 님
func('홍길동', '안녕')       # 홍길동 !!!! 안녕 님

# (3) 키워드인자(keyword argument)  : 키워드에 알맞은 위치에 값이 대입된다.
func(name='홍길동', greeting='안녕')

# (4) 인자의 기본값 : 인자의 기본값을 지정함으로써 인자가 들어오지 않을 경우에 대한 에러를 방지할 수 있다
def func(greeting, name="홍길동"):
    print(greeting, '!!!!',  name, '님')
# 해당 경우처럼 name 값 설정한 경우는 설정한 값으로 출력
func('하이', '박길동')       # 하이 !!!! 박길동 님
# 해당 경우는 name에 대한 인자값이 없기 때문에 기본값이 출력
func('안녕')


'''
#----------------------------------------------------------------
# (5) 위치 인자 모으기 (*) -- * args

첫번째와 두번째는 인자가 반드시 들어가고 세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 네번째 인자부터는 정확히 모른다면?

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # args에 7,8,9가 튜플로 들어간다
'''

# 첫번째와 두번째는 인자가 반드시 들어가고 세번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다.
# 그러나 네번째 인자부터는 정확히 모른다면 위치 가변인자를 사용하여 값을 받고 튜플에 지정할 수 있다.
def func(a, b, c=0, *args ):
    sum = a + b + c
    for i in args:
        sum += i
    return sum

print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))

#----------------------
# (5) 키워드 인자 모으기 -- ** kwargs
# key=value로 구성된 인자가 여러 개 들어오고, 얼만큼 들어올지 모르는 경우에
#  키워드 가변인자로 값을 받고 딕셔너리에 지정할 수 있다.
def func(a, b, c=100, *args, **kwargs):
    sum = a + b + c
    for i in args:
        sum += i
    for k in kwargs:
        sum +=kwargs[k]
    return sum

print(func(10, 20))
print(func(1, 2, 3))
print(func(1, 2, 3, 4, 5, 6))
print(func(1, 2, kor=10, eng=20))
print(func(1, 2, 3, 4, java=5, math=6))


#--------------
# 1번 1 {1,3,4,5}
list_1 = [0, 3, 1, 7, 5, 0, 5, 8, 0, 4]
def quiz_2(list_data):
	a = set(list_data)
	return list(a)[1:5]

print(quiz_2(list_1))

# 2번 False
def  delete_a_list_element(list_data, element_value):
	if element_value in list_data:
		list_data.remove(element_value)
		return list_data
	else:
		return "False"

list_data = ['a', 1, 'gachon', '2016.0']
element = float(2016)
result = delete_a_list_element(list_data, element)
print(result)

# 3번 1번
tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
def quiz_1(tuple_1, tuple_2):
	result = []
	for i in (tuple_1 + tuple_2):
		result.append(i)
	return result

print(quiz_1(tuple_1, tuple_2))

# 연습문제
# 1
def even_filter(alist):
    result =[]
    for i in alist:
        if i%2 == 0:
            result.append(i)
    return result

print(even_filter([1, 2, 4, 5, 8, 9, 10]))

# 2번
def is_prime_number(num):
    for i in range(2, int(num/2)):      # 2로 나누어지는 것은 이미 소수가 아님
        if num % i == 0:
            return False
    return True
print(is_prime_number(60))
print(is_prime_number(61))

# 3번
def count_vowel(tt):
    count = 0
    for i in tt:
        if i in ('a', 'e', 'i', 'o', 'u'):
            count += 1
    return count

print(count_vowel("pythonian"))

def count_vowel2(words):
   vowel = ['a','e','i','o','u']
   cnt = 0
   for i in vowel:
      cnt += words.count(i)
   return cnt

print(count_vowel2("pythonian"))