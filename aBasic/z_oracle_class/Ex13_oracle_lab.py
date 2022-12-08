"""
0. DB에 저장할 테이블 생성
1. 사용자 입력 받아 확인
2. 모든 연락처 출력하기
3. 연락처 삭제하기
"""
import cx_Oracle as oci

class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name=name
        self.phone_name=phone_number
        self.email=email
        self.addr=addr

    def print_info(self):
        print("이름:", self.name)
        print("전화번호:", self.phone_name)
        print("이메일:", self.email)
        print("주소;", self.addr)

def createDBTable():
    # 1. 연결객체 얻어오기(Connection)
    # 계정명 / 비밀번호 / @ / IP / 오라클 포트번호 / xe
    conn = oci.connect('scott/tiger@192.168.0.26:1521/xe')
    print(conn.version)
    # 2. sql 문장
    sql = '''
        CREATE TABLE user_info
        (
            name   varchar2(50),
            phone_number  varchar2(50),
            email     varchar2(100),
            addr    varchar2(100)
        )
    '''
    # 3. cursor 객체 얻어오기
    cursor = conn.cursor()
    # 4. 실행
    cursor.execute(sql)
    # # 5. cursor 객체 닫기
    cursor.close()
    # # 6. 연결객체 닫기
    conn.close()

def print_menu():
    print('1. 연락처 입력')
    print('2. 연락처 출력')
    print('3. 연락처 삭제')
    print('4. 종료')
    menu=input('메뉴선택:')
    return int(menu)

def set_contact():
    # (1)
    # 이름, 전화번호, 이메일, 주소를 입력받아
    name = input('이름은?')
    phone_number = input('전화번호는?')
    email = input('이메일은?')
    addr = input('주소는?')

    # 1. 연결객체 얻어오기(Connection)
    conn = oci.connect('scott/tiger@192.168.0.26:1521/xe')
    # 2. sql 문장
    #sql = '''insert into user_info Values ('{0}', '{1}', '{2}', '{3}')'''.format(name, phone_number, email, addr)
    sql = 'INSERT INTO user_info VALUES(:0,:1,:2,:3)'
    '''
    :(콜론) : 이후에 변수명 대신 다른 문자를 넣어도 갯수만 맞으면 동일하게 실행되지만,
    혼동을 피하기 위해서 변수명을 사용하는 편이 좋다. 
    
    '''
    # 3. cursor 객체 얻어오기
    cursor = conn.cursor()
    # 4. 실행
    cursor.execute(sql, [name, phone_number, email, addr])
    # 5. cursor 객체 닫기
    cursor.close()
    # commit 잊지말자
    conn.commit()
    # 6. 연결객체 닫기
    conn.close()
    # Contact 객체를 생성하고 DB 에 입력

def print_contact():
    # (2)
    #  테이블의 전체 레코드 출력
    # 1. 연결객체 얻어오기(Connection)
    conn = oci.connect('scott/tiger@192.168.0.26:1521/xe')
    # 2. sql 문장
    sql = 'SELECT * FROM user_info '
    # 3. cursor 객체 얻어오기
    cursor = conn.cursor()
    # 4. 실행
    cursor.execute(sql)
    # print(datas)  # turple 형식으로 출력
    for row in cursor.fetchall():
        print('이름:', row[0])
        print('전화번호:', row[1])
        print('이메일:', row[2])
        print('주소:', row[3])
        print('--------')
    # 5. cursor 객체 닫기
    cursor.close()
    # 6. 연결객체 닫기
    conn.close()

def delete_contact(name):
    # (3)
    # 해당이름과 같은 요소를 찾아서 삭제
    # 1. 연결객체 얻어오기(Connection)
    conn = oci.connect('scott/tiger@192.168.0.26:1521/xe')
    # 2. sql 문장
    #sql = 'DELETE FROM user_info WHERE name= :0 '
    sql = 'DELETE FROM user_info WHERE name= ' + name
    # 3. cursor 객체 얻어오기
    cursor = conn.cursor()
    # 4. 실행
    cursor.execute(sql)
    # cursor.execute(sql, name)
    # 5. cursor 객체 닫기
    cursor.close()
    conn.commit()
    # 6. 연결객체 닫기
    conn.close()

def run():
    while True:
        menu=print_menu()
        if menu==4:  # 종료를 선택하면
            break
        elif menu==1: # 입력을 선택하면
            set_contact()
        elif menu==2: # 출력을 선택하면
            print_contact()
        elif menu==3: # 삭제를 선택하면
            name = input('삭제할 이름은?')
            delete_contact(name)


if __name__ == "__main__":
    #createDBTable()
    run()
    # (1) 테이블 생성

