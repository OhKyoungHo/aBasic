# 부울형 (논리형)- 첫글자는 반드시 대문자 True, False, None 여야 한다
t = True
f = False
n = None    # 다른 언어의  null 값과 유사

hungry = True
sleepy = False
print(not hungry)   # False
print(hungry and sleepy)   # False
print(hungry or sleepy)   # True

# 연산자 기호 쓰는 것은 권장하지 않음
print(hungry & sleepy)   # False
print(hungry | sleepy)   # True

"""
        자료형         값           부울형
    -----------------------------------------------------
        문자형       "문자"          True    문자가 하나라도 있으면
                    ""                     False    문자가 없으면
        리스트       [1,2,3]         True          리스트가 하나라도 있으면
                    []                     False    리스트가 없으면
        튜플         ()                     False     없는 경우
        딕셔너리     {}                     False      없는 경우
        숫자형       0이아닌 숫자     True
                    0                      False    숫자가 0이면
                    None                   False    숫자가 없으면
                    """


if('아'):        #  True
    print('True')
else:
    print('False')



if([]):    # False2
    print('True2')
else:
    print('False2')


if 0:      #  False3
    print('True3')
else:
    print('False3')

if -1:  # True4
    print('True4')
else:
    print('False4')

msg ='행복합시다'
#find는 해당 index를 찾기 때문에 해당 find로 통해서 찾은 '행' 이 0번째 순서라서 False로 나오기 때문에 no 출력
if msg.find('행'):   #no
    print('ok')
else:
    print('no')

msg = '행복합시다'
if msg.find('가'):  # 없어서 -1이기 때문에 ok
    print('ok')
else:
    print('no')

msg ='행복합시다' # no
if(msg.find('가') > -1):
    print('ok')
else:
    print('no')

if '행' in msg:
    print('ok')
else:
    print('no')




