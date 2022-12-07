class Sample:
    # 생성자(초기화)
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 필요한 매직메소드를 추가
    # 생성자에서 지정된 멤버 변수의 값을 출력하기 위해 JAVA의 toString( )  같은 개념
    def __str__(self):
        return '이름:{}, 나이:{}'.format(self.name, self.age)   # self를 붙여줘야 오류 안남(정확한 값을 받아롬)

    # 생성자에서 지정된 멤버 변수의 값에 더하기 연산 결과를 출력
    def __add__(self, other):
        self.age += other
    # 생성자에서 지정된 멤버 변수의 값과 특정 값을 비교한 결과를 출력하기 위해
    def __ge__(self, other):
        if self.age >= other:
            return "성인"
        else:
            return "미성년"

s=Sample('홍길동', 22)
print(s)
s+10
print(s)
print(s >= 20)



"""
    매직 메소드

(1) Binary Operators
        Operator	Method
        +	    object.__add__(self, other)
        -	    object.__sub__(self, other)
        *	    object.__mul__(self, other)
        //	    object.__floordiv__(self, other)
        /	    object.__div__(self, other)
        %	    object.__mod__(self, other)
        **	    object.__pow__(self, other[, modulo])
        >>	    object.__lshift__(self, other)
        <<	    object.__rshift__(self, other)
        &	    object.__and__(self, other)
        ^	    object.__xor__(self, other)
        |	    object.__or__(self, other)  
        
(2) Comparison Operators
        Operator	Method
        <	    object.__lt__(self, other)
        <=	    object.__le__(self, other)
        ==	    object.__eq__(self, other)
        !=	    object.__ne__(self, other)
        >=	    object.__ge__(self, other)
        >	    object.__gt__(self, other)
                
(3) Extended Assignments
        Operator	Method
        +=	    object.__iadd__(self, other)
        -=	    object.__isub__(self, other)
        *=	    object.__imul__(self, other)
        /=	    object.__idiv__(self, other)
        //=	    object.__ifloordiv__(self, other)
        %=	    object.__imod__(self, other)
        **=	    object.__ipow__(self, other[, modulo])
        <<=	    object.__ilshift__(self, other)
        >>=	    object.__irshift__(self, other)
        &=	    object.__iand__(self, other)
        ^=	    object.__ixor__(self, other)
        |=	    object.__ior__(self, other)
          
(4) Unary Operators
        Operator	Method
        -	        object.__neg__(self)
        +	        object.__pos__(self)
        abs()	    object.__abs__(self)
        ~	        object.__invert__(self)
        complex()	object.__complex__(self)
        int()	    object.__int__(self)
        long()	    object.__long__(self)
        float()	    object.__float__(self)
        oct()	    object.__oct__(self)        
        hex()	    object.__hex__(self)
"""


class Person(object):
    def __init__(self, name):
        self.name = name

    def language(self):
        pass

class Earthling(Person):
    def language(self, language):
        return language

class Groot(Person):
    def language(self, language):

        return "I'm Groot!"

name = ['Gachon', 'Dr.Strange', 'Groot']

country = ['Korea', 'USA', 'Galaxy']

language = ['Korean', 'English', 'Groot']

for idx, name in enumerate(name):
    if country[idx].upper() != 'GALAXY':
        person = Earthling(name)
        print(person.language(language[idx]))
    else:
        groot = Groot(name)
        print(groot.language(language[idx]))


class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, back_number):
        self.back_number = back_number

jinhyun = SoccerPlayer("jinhyun", "MF", 10)
print("현재 선수의 등번호는:", jinhyun.back_number)
jinhyun.change_back_number(5)
print("현재 선수의 등번호는:", jinhyun.back_number)


class Marvel(object):
    def __init__(self, name, characteristic):
        self.name = name
        self.characteristic = characteristic
    def __str__(self):

        return "My name is {0} and my weapon is {1}.".format(self.name, self.characteristic)

class Villain(Marvel):
    pass

first_villain = Villain("Thanos", "infinity gauntlet")
print(first_villain)


class TV(object):


    def __init__(self, size, year, company):
        self.size = size
        self.year = year
        self.company = company

    def describe(self):
        print(self.company + "에서 만든 " + self.year + "년형 " + self.size + "인치" + "TV")

class Laptop(TV):
    def describe(self):
        print(self.company + "에서 만든 " + self.year + "년형 " + self.size + "인치 " + "노트북")

LG_TV = TV("32", "2019", "LG")
LG_TV.describe()
samsung_microwave = Laptop("15", "2018", "Samsung")
samsung_microwave.describe()


class Score:

    def __init__(self, student):
        tmp = student.split(",")
        self.name = tmp[0]
        self.midterm = int(tmp[1])
        self.final = int(tmp[2])
        self.assignment = int(tmp[3])
        self.score = None
        self.grade = None

    def total_score(self):

        test_score = ((self.midterm + self.final) / 2) * 0.8
        if self.assignment >= 3:
            assign_score = 20
        elif self.assignment >= 2:
            assign_score = 10
        elif self.assignment >= 1:
            assign_score = 5
        else:
            assign_score = 0
        self.score = test_score + assign_score

    def total_grade(self):

        if self.assignment == 0:
            grade = "F"
        elif self.score >= 90:
            grade = "A"
        elif self.score >= 70:
            grade = "B"
        elif self.score >= 60:
            grade = "C"
        else:
            grade = "F"
        self.grade = grade
        return grade


student_john = Score("john,90,90,0")

aa = student_john.total_score()

bb = student_john.total_grade()

print(aa, bb, student_john.score, student_john.grade)

'''
student_john = Score("john,90,90,0") 일 경우,

(1) total_score() 는 return 이 없기 때문에 None 출력
(2) total_grade() 는 return 이 grage 이며 assignment 값에 따라 지정되므로 F 출력
    int(tmp[3]) = 0
    self.assignment = int(tmp[3])
    if self.assignment==0:
        grade = "F"
(3) score 는 test_score + assign_score 이고
    test_score 는 ((self.midterm + self.final)/2)*0.8 의 결과값인 72.0 가 된다. 
(4) grade 는 self.grade = None 이었다가 total_grade( ) 함수에서 self.grade = grade 로 다시 지정된다.
    if self.assignment==0:
        grade = "F"
'''