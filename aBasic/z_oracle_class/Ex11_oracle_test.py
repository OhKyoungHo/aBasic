# [ 파이썬 + 디비 절차 ]
# 1. 연결객체 얻어오기(Connection)
# 2. sql 문장
# 3. cursor 객체 얻어오기
# 4. 실행
# 5. cursor 객체 닫기
# 6. 연결객체 닫기

import cx_Oracle as oci
# 1. 연결객체 얻어오기(Connection)
# 계정명 / 비밀번호 / @ / IP / 오라클 포트번호 / xe
conn = oci.connect('scott/tiger@192.168.0.26:1521/xe')
print(conn.version)
# 2. sql 문장
sql = 'select * from emp'
# 3. cursor 객체 얻어오기
cursor = conn.cursor()
# 4. 실행
cursor.execute(sql)
datas = cursor.fetchall()
# print(datas)  # turple 형식으로 출력
for row in datas:
    print(row[0], row[1], row[2])
# 5. cursor 객체 닫기
cursor.close()
# 6. 연결객체 닫기
conn.close()
