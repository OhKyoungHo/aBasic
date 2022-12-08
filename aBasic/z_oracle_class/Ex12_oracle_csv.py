# [ 파이썬 + 디비 절차 ]
# 1. 연결객체 얻어오기(Connection)
# 2. sql 문장
# 3. cursor 객체 얻어오기
# 4. 실행
# 5. cursor 객체 닫기
# 6. 연결객체 닫기
import cx_Oracle as oci
import csv

def createDBTable():
    # 1. 연결객체 얻어오기(Connection)
    # 계정명 / 비밀번호 / @ / IP / 오라클 포트번호 / xe
    conn = oci.connect('scott/tiger@192.168.0.26:1521/xe')
    print(conn.version)
    # 2. sql 문장
    sql = '''
        CREATE TABLE supply
        (
            id              number primary key,
            Supplier_Name   varchar2(50),
            Invoice_Number  varchar2(50),
            Part_Number     varchar2(50),
            Cost            number,
            Purchase_Date   date
        )
    '''
    # 3. cursor 객체 얻어오기
    cursor = conn.cursor()
    # 4. 실행
    cursor.execute(sql)
    sql2 = 'create sequence seq_supply_id'
    cursor.execute(sql2)
    # 5. cursor 객체 닫기
    cursor.close()
    # 6. 연결객체 닫기
    conn.close()

def saveDBTable(data):
    # 1. 연결객체 얻어오기(Connection)
    conn = oci.connect('scott/tiger@192.168.0.26:1521/xe')
    # 2. sql 문장
    sql = '''
    INSERT INTO supply
    VALUES(seq_supply_id.NEXTVAL, :0,:1,:2,:3,:4)
    '''
    # 3. cursor 객체 얻어오기
    cursor = conn.cursor()
    # 4. 실행
    cursor.execute(sql, data)
    # 5. cursor 객체 닫기
    cursor.close()
    # commit 잊지말자
    conn.commit()
    # 6. 연결객체 닫기
    conn.close()

def viewDBTable(tableName):
    # 넘겨받은 테이블명의 데이터를 화면에 출력
    # 1. 연결객체 얻어오기(Connection)
    conn = oci.connect('scott/tiger@192.168.0.26:1521/xe')
    # 2. sql 문장
    sql = 'SELECT * FROM ' + tableName
    # 3. cursor 객체 얻어오기
    cursor = conn.cursor()
    # 4. 실행
    cursor.execute(sql)

    # print(datas)  # turple 형식으로 출력
    # fetchall( ) 함수를 사용하여 SELECT 문으로 검색한 결과를 모두 가져온 뒤, 변수 rows 에 담는다.
    # 변수 rows 에 들어있는 데이터는 여러 줄로 이루어져 있으므로, for 반복문을 사용하여 list 자료형으로 출력된다.
    for row in cursor.fetchall():
        print(row)
    # 5. cursor 객체 닫기
    cursor.close()
    # 6. 연결객체 닫기
    conn.close()



if __name__ =='__main__':
    # (1) 테이블 생성
    #createDBTable()

    # (2) 입력 확인
    #imsi =['kosmo', '9999', '8888', 1000, '2022-12-08']
    #saveDBTable(imsi)

    # (3) csv 파일을 읽어서 db에 입력
    # file = open('supply.csv','r')
    # datas = csv.reader(file)
    #
    # header = next(datas, None)
    # print(header)
    # print('_'*50)
    # for row in datas:
    #     #print(row)
    #     saveDBTable(row)

    # (4) 값들을 출력
    viewDBTable('supply')
