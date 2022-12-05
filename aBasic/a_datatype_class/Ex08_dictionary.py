"""
    [ dictionary 형 ]

    1- 키와 값으로 구성 ( 자바의 map 와 유사 )
    2- 저장된 자료의 순서는 의미 없음
    3- 중괄호 {} 사용
    4- 변경가능
    ※ tuple만 값 변경 불가

    ` 사전.keys() : key만 추출 (임의의 순서)
    ` 사전.values() : value만 추출 (임의의 순서)
    ` 사전.items() : key와 value를 튜플로 추출 (임의의 순서)
"""

print('--------- 1. 딕셔너리 요소 --------------- ')
dt = {1:'one', 2:'two', '3':'three'}
print(dt)
print(dt[1])    #one
print(dt['3'])  #three(해당 키값이 문자라서 '3' 형태로 써줘야 함)


# 키는 숫자와 문자 그리고 튜플이여야 한다. 즉 리스트는 안된다.
# 리스트의  값이 변경 가능하다. 그러나 키값을 변경하면 안되므로 리스트는 안된다
dt2 = {1:'one', 2:'two', (3,4):'turple'}
print(dt2[(3,4)])   #turple

# turple 값을 python으로 변경
dt2[(3,4)] ='python'
print(dt2[(3,4)])

print('--------- 2. 딕셔너리 추가 및 수정  --------------- ')
# 딕셔너리에 값 추가
dt2['korea'] ='seoul'
print(dt2)

# 딕셔너리에 값 수정
#'seoul' -> '한국'
dt2['korea'] ='한국'
print(dt2)

# 여러개 추가할 때
dt2.update({5: 'five', 6: 'six'})
print(dt2)

print('--------- 3. Key로 Value값 찾기  --------------- ')
print(dt2.keys())        #list 형태
print(dt2.values())      #list 형태
print(dt2.items())       #turple을 list로 뽑아줌

# Key와 Value만 따로 검색

#  1번 (가)stack (나)queue (다)turple (라)set

# 2번 1.2019
a = [3, "apple", 2016, 4]
b = a.pop(0)    #3
print(b)
c = a.pop(1)    #2016
print(b + c)    #2019

# 3번 4
dict_1 = {2:1, 4:2, 6:3, 8:4, 10:6}
dict_keys = list(dict_1.keys())
dict_values = list(dict_1.values())
dict_2 = dict()
for i in range(len(dict_keys)):
	dict_2[dict_values[i]] = dict_keys[i]

print(dict_2[2])    #키값이 2인거 출력


# 4번 1. {4: 'ant', 'ant': 6, 0: 'snake', 2: 'monkey', 8: 'spider'}
animal = ['cat', 'snake', 'monkey', 'ant', 'spider']
legs= [4, 0, 2, 4, 8]
animal_legs_dict = {}
for i in range(len(animal)):
	animal_legs_dict[legs[i]] = animal[i]
	animal_legs_dict['ant'] = 6

print(animal_legs_dict)

# 5번 10
Mydict = {'1' : 1, '2' : 2}
Copy = Mydict
Mydict['1'] = 5
result= Mydict['1'] + Copy['1']
print(result)

#6번
a = list(range(10))
print(a)
a.append(a[3])
print(a)
a.pop(a[3])
print(a)
a.insert(3, a[-1])
print(a)
a.pop()
print(a)

#7번
data_1 = {'one' : (1,2,3,4,5,6), 'two' : [1,2,3,4,5,6], 'three' : {'four' : 4, 'five' : 5}}
for k in ['one','two','three']:
	try:
		print(data_1[k][:1])
	except TypeError:
		print("error")
# dict은 배열 형태로 쓸 수 없다 그래서 error 발생

for k in ['one', 'two','three']:
	try:
		data_1[k][-1] = "a"
		#three 부터 출력
		print(data_1[k][-1])
	except TypeError :
		print("error")
		#처음부터 error나오고 나머지는 a
