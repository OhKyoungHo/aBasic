"""
    @ 컴프리핸션 (comprehension)
    ` 하나 이상의 이터레이터로부터 파이썬 자료구조를 만드는 컴팩트한 방법
    ` 비교적 간단한 구문으로 반복문과 조건 테스트를 결합

    * 리스트 컨프리핸션
        [ 표현식 for 항목 in 순회가능객체 ]
        [ 표현식 for 항목 in 순회가능객체 if 조건 ]

    * 딕셔러리 컨프리핸션
        { 키_표현식: 값_표현식 for 표현식 in 순회가능객체 }

    * 셋 컨프리핸션
        { 표현식 for 표현식 in 순회가능객체 }

    * 튜플은 컨프리핸션이 없다

"""


# 컨프리핸션 사용하지 않은 리스트 생성
alist = []
alist.append(1)
alist.append(2)
alist.append(3)
alist.append(4)
alist.append(5)
alist.append(6)
print(alist)

alist = []
for n in range(1, 7):
    alist.append(n)
print(alist)

alist = list(range(1,7))
print(alist)


#------------------------------------------------
# 리스트 컨프리핸션
blist =[ n for n in range(1, 7)]
print(blist)

blist =[ n**2 for n in range(1, 7)]
print(blist)

blist =[ n for n in range(1, 7) if n%2==1 ]
print(blist)

# 컨프리핸션이 아닌 코드를 컨프리핸션으로 변경
clist =[]
for r in range(1,4):
    for c in range(1,3):
        clist.append( (r, c) )
print(clist)

dlist = [(r, c) for r in range(1, 4) for c in range(1, 3)]
print(dlist)

data = (1, 2, 3, 2, 1, 4, 5)
alist = [ n for n in data]
print(alist)


#-------------------------------------------
# 딕셔러니 컨프리핸션
data = (2, 3, 4)
adic = { n : n**2 for n in data }
print(adic)

# word에서 한 글자씩 추출하여 letter라는 변수에 지정하고,
# 각 글자 : word에 있는 글자의 갯수
# 로 딕셔너리 구조를 만든다.
word = 'LOVE LOL'
# set을 설정함으로써 'L'을 찾는 과정을 한번으로 줄였다
# 만약 안했으면 'L' 찾는 과정을 3번을 했다
# set을 통해 중복되는 단어찾는 과정을 줄여준다
wcnt = { letter : word.count(letter) for letter in set(word) }
wcnt1 = { letter : word.count(letter) for letter in word }
print(wcnt)
print(wcnt1)
#------------------------------------------------
# 셋 컨프리핸션
data = (1, 2, 3, 2, 1, 4, 5)
bset = { n for n in data}
print(bset)  # 중복해서 나오지 않음

'''
#------------------------------------------------
# 프로젝트할 때 팀구호'''
우리의결의= """취하고싶으면달려라
맡은업무는반드시마치자
노력없는성과는없다
구글신과함께공부하자"""

result = [ j[i*2] for i, j in enumerate(우리의결의.splitlines())]
print(result)
print(우리의결의.splitlines())


# -------------------------------------------------
# 프로젝트할 때 팀구호
우리의결의= """취하고싶으면달려라 
맡은업무는반드시마치자 
노력없는성과는없다 
구글신과함께공부하자"""
result = [ j[i*2] for i, j in enumerate(우리의결의.split('\n'))]
print(result)


#---------------------
# 1번 3
mylist = ['apple' ,'banana', 'grape']
result = list(enumerate(mylist))
print(result)

# 2번 4
cat_song = "my cat has blue eyes, my cat is cute"
print({i:j for j,i in enumerate(cat_song.split())})

# 3번 orange&pink&brown&black&white
colors = ['orange', 'pink', 'brown', 'black', 'white']
result = '&'.join(colors)
print(result)

#4번 {'students': 0, 'superuser': 1, 'professor': 2, 'employee': 3}
user_dict = {}
user_list = ["students","superuser", "professor", "employee"]
for value_1, value_2 in enumerate(user_list):
    user_dict[value_2] = value_1
print(user_dict)

'''
user_list = ["students","superuser", "professor", "employee"] 일 때,
enumerate(user_list) == (0, students), (1, superuser), (2, professor), (3, employee)

user_dict[value_2] = value_1 에서 value_2가 key가 되고 value_1이 value가 되므로,
{'students': 0, 'superuser': 1, 'professor': 2, 'employee': 3}
'''

# 6번 ['Cat', 'Panda', 'Owl']
animal = ['Fox', 'Dog', 'Cat', 'Monkey', 'Horse', 'Panda', 'Owl']
print([ani for ani in animal if 'o' not in ani])

# 7번 DongUniversity
name = "Hanbit University"
student = ["Hong", "Gil", "Dong"]
split_name = name.split()
print(split_name)
join_student = ''.join(student)
print(join_student)
print(join_student[-4:] + split_name[1])

# 8번 zip
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2' ,'b3']
for a, b in zip(alist, blist):
    print(a, b)

# 9번
a = [1, 2, 3]
b = [4, 5, ]
c = [7, 8, 9]
print([[sum(k), len(k)] for k in zip(a, b, c)])

# 10번 yellow
week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
list_data = [week, rainbow]
print(list_data[1][2])

# 11번 score: 72
kor_score = [30, 79, 20, 100, 80]
math_score = [43, 59, 0, 30, 90]
eng_score = [49, 72, 48, 67, 15]
midterm_score = [kor_score, math_score, eng_score]
print ("score:",midterm_score[2][1])

# 12번 ['a', '2', 'error']
alist = ["a", "b", "c"]
blist = ["1", "2", "3"]
abcd= []
for a, b in enumerate(zip(alist, blist)):
    try:
        abcd.append(b[a])
    except IndexError:
        abcd.append("error")

print(abcd)

'''
zip(alist, blist) 는 ('a', '1') ('b', '2') ('c', '3') 이고,
enumerate() 를 적용하면 
(a, b)의 튜플 구조를 갖는 (0, ('a', '1')) (1, ('b', '2')) (2, ('c', '3')) 가 된다. 
a : 0, 1, 2
b : ('a', '1'), ('b', '2'), ('c', '3')
따라서, b[a] 는 ('a', '1')[0] == 'a'
                ('b', '2')[1] == '2'
                ('c', '3')[2] == 없음 .. 'error'
실행결과 abcd = ['a', '2', 'error'] 가 출력된다. 
'''

# 13번 80
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h"]
nums = [i for i in range(20)]
print(nums)
answer = [alpha+str(num) for alpha in alphabet for num in nums if num%2==0]
print(answer)
print(len(answer))
