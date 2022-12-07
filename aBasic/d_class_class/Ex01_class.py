"""
     1) 클래스 기초

     ` __init__ 함수 : 객체 초기화 함수( 생성자 역할 )
     ` self : 객체 자신을 가리킨다.
"""
'''
자바인 경우
class Sample {
    String data = "Hello";
    String name;
    Sample(String name){
        this.name = name;
    }
}

Sample s = new Sample("홍길동");
'''
#  * def __init__(self) : 는 생성자 역할을 하며, 여기서 self는 this의 의미로 Sample 클래스를 가리킨다.
#  생성자 안에서 self 를 붙여 멤버변수를 선언할 수 있다.
#  생성자에서 아무것도 하지 않으려면 pass를 기술한다.

class Sample:
    data = 'Hello'
    # 생성자 역할
    def __init__(self, name, age):
        self.name = name            # 멤버변수 선언
        self.age = age
        print('__init__호출')
    # 소멸자 역할 : 클래스가 끝나는 지점을 알려준다
    def __del__(self):
        print('__del__호출')

s = Sample('홍길동',20)
print(s.data)
print(s.name)
print(s.age)
# 클래스의 메모리를 해제하려면 del 키워드를 사용한다.
del s

print('-'*20)


"""
    2) 
    인스턴스 함수 :  'self'인 인스턴스를 인자로 받고 인스턴스 변수와 같이 하나의 인스턴스에만 한정된 데이터를 생성, 변경, 참조
    클래스   함수 :  'cls'인 클래스를 인자로 받고 모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조
     
    - 클래스 함수는 클래스명 접근
 
 [자바인 경우]
 class Sample{
    int a;
    static int b;
 }
 Sample s1 = new Sample();
 Sample s2 = new Sample();
 Sample s3 = new Sample();
 
 s1.a, s2.a, s3.a은 다 다른 값이다
 but s1.b, s2.b, s3.b 는 같은 값을 참조한다
"""
class Book:
    cnt = 0
    #생성자
    def __init__(self, title):
        # 매개변수(지역)을 멤버변수로 지정
        # self는 현재의 객체를 가리키는 변수
        self.title = title
        self.cnt += 1

    # 인스턴스 함수 : 클래스 안의 일반 함수
    def ouput(self):
        pass
    # 클래스 함수
    @classmethod    # static과 유사하다고 생각(하나의 객체에서만 참조)
    def output2(cls):
        cls.cnt += 1

b1 = Book('행복이란')
b2 = Book('먹고살자')
Book.output2()
Book.output2()
print(Book.cnt)     # 2

'''
     3) 클래스 상속
        - 파이션은 method overriding은 있지만 method overloading 개념은 없다
        - 파이션은 다중상속이 가능
        - 부모 클래스가 2개 이상인 경우 먼저 기술한 부모클래스에서 먼저 우선 해당 멤버를 찾음
'''
class Animal:
    def move(self):
        print('동물은 움직인다')

class Human(Animal):
    def move(self):
        print('인간은 두발로 걷는다')
class Wolf(Animal):
    def move(self):
        print('늑대는 네 발로 달린다')

#  부모 클래스가 2개 이상인 경우에는 먼저 기술한 부모 클래스에서 해당 멤버를 찾아 출력한다.
class WereWolf(Human, Wolf):
    def move(self):
        print('늑대인간은 두 발로 달린다')
print('-'*20)
ww = WereWolf()
ww.move()

h = Human()
h.move()

w = Wolf()
w.move()

