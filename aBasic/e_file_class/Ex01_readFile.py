"""
@ 파일 읽고 쓰기
    - 파일을 읽고 쓰기 전에 파일을 열어야 한다
    - fileObj = open ( filename, mode )
            mode 첫번째 글자 - 작업 표시
            r(read)  : 파일 읽기
            w(write) : 파일 쓰기 ( 파일이 없으면 생성하고 파일이 있으면 덮어쓴다 )
            x(write) : 파일 쓰기 ( 파일이 없을 때만 생성하고 쓴다 )
            a(append) : 파일 추가 ( 파일이 있으면 파일의 끝에서부터 추가하여 쓴다 )

            mode 두번째 글자 - 파일 타입
            t : 텍스트(text) 타입 ( 기본값 )
            b : 이진(binary) 타입
            두번째 글자가 없으면 텍스트 타입이다.

            encoding='utf-8' : 한글

    - 파일을 열고 사용 후에는 반드시 닫아야 한다( close() )
    - 간단한 파일의 경우 별다른 문제가 없으나,
         다수의 파일로 작업할 경우, 원치 않는 데이터 처리가 발생할 수 있기 때문에 필요한 작업 직후 닫아준다.
         (통로는 기본적으로 바로 닫아주기 ! )
    - 파일 객체를 자동으로 닫는 with 구문을 많이 사용한다.
"""
'''
# 상대경로
# 해당 파일을 열고 , 파일을 읽을 거고 한글 처리
# 만약 파일이 없는 경우 에러 발생
try:
    f = open('./data/data.txt', 'r', encoding='utf-8')
except FileNotFoundError as e:
    print('파일을 찾을 수 없습니다 >',e)
else:
    # 반복문을 사용하여 파일을 한 줄씩 읽다가 더 이상 내용이 없을 경우 반복문을 빠져나가게 하기
    while True:
        line = f.readline()     #  readline( ) : 한 줄을 읽어오기. 
        if not line: break
        print(line)
    f.close         # 파일을 열고 사용한 경우에는 반드시 닫아야 한다
finally:
    print('종료')
'''

# 자동으로 close() 하기 위해 with 구문
# with 구문 : 파일을 열고 데이터를 읽는 작업이 끝난 뒤, 자동으로 파일 객체를 (close)닫아준다.
# with open('data/data.txt', 'r', encoding='utf=8') as f:
#     while True:
#         line = f.readline()
#         if not line: break
#         print(line)

fileName = './data/' + 'data.txt'
with open(fileName, 'r', encoding='utf-8') as f:
    content = f.read()  # 전체 통으로 읽음
    words = content.split()  # 잘라서 words에 담기
print(content)
print('총단어수 : ', len(words))

# 예외 처리 문장
try:
    with open('data/data.txt', 'r', encoding='utf=8') as f:
        content = f.read()  # read() :파일을 통으로 읽어줌
        words = content.split()  # 파일을 띄어쓰기 기준으로 나눔
except FileNotFoundError:
    print('파일을 찾을 수 없습니다')
else:
    print(content)
    print('총 단어수 : ', len(words))
finally:
    print('종료')
