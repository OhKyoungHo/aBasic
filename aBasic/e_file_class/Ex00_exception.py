"""
    [에러와 예외]
    1. 에러 : 어떤짓을 해도 실행 x
        문법적 오류
    2. 예외 : 어떠한 조치를 한다면 실행은 가능
        실행시 발생하는 오류로 예외가 발생하면 프로그램이 비정상 종료된다

    [예외처리]
    try:
        예외 발생 가능 문장들
    except Exception:
        예외가 발생한 후에 실행할 문장들
    else:
        예외가 발생하지 않았을 때 실행되는 문장들
    finally:
        예외 발생 여부와 상관없이 무조건 실행되는 문장들

    [참고] 파이썬 내장 예외
        https://docs.python.org/3/library/exceptions.html
"""

# 0으로 나누기
#(1)
# 컴퓨터는 0으로 나눌경우 예외 발생
#10/0 # -> 예외발생 : ZeroDivisionError: division by zero

# (2)
# 예외가 발생할거 같은 문장을 try안에 넣어주기
try:
     10/0
except Exception:
#  예외가 발생할 경우의 수행할 작업 지정
    print("예외")

# (3)
try:
     10/0
# as 를 사용하여 예외에 별칭을 넣어서 예외가 발생했을 때 에러 내용을 출력할 수 있다.
except Exception  as e:
    print("예외:", e)


try:
     10/0
# as 를 사용하여 예외가 발생했을 때 에러 내용을 출력할 수 있다.
except Exception  as e:
    print("예외:", e)
# finally를 사용하여 예외 발생 여부와 상관없이 무조건 실행
finally:
    print('무조건 수행')

try:
     10/1
# as 를 사용하여 예외가 발생했을 때 에러 내용을 출력할 수 있다.
except Exception  as e:
    print("예외:", e)
# else를 사용하여 예외가 발생하지 않았을 때 실행
else:
    print('예외가 없는 경우')
# finally를 사용하여 예외 발생 여부와 상관없이 무조건 실행
finally:
    print('무조건 수행')
