
import datetime
today = datetime.date.today()
# today is  2022-12-05(오늘 날짜)
print('today is ', today)

# datetime에 있는 date만 import
from datetime import date, timedelta
today = date.today()
# today is  2022-12-05(오늘 날짜)
print('today is ', today)

tod = ['월', '화', '수', '목', '금', '토', '일']
number = date.today().weekday()

#날짜 구하기
print('년도 : ', today.year)
print('월 : ', today.month)
print('일 : ', today.day)
print('요일 : ', tod[number])

# 날짜 계산
print('어제 : ', today + timedelta(days=-1))

# 일주일전 날짜
print('일주일 전 : ', today + timedelta(days=-7))
print('일주일 전: ', today + timedelta(weeks=-1))


# 10일 후 날짜
print('10일 후 : ', today + timedelta(days=+10))

# 1번경우
from datetime import datetime
day = datetime.today()
print(day)
# 2번 경우
# import datetime
# day = datetime.datetime.today()
# print(day)

# 날짜를 문자열 형태( strftime() 이용)(대소문자 구별 필요 M이 분, m이 월)
print(day.strftime('%Y년 %m월 %d일 %H시:%M분'))

# 문자열을 날짜 형태( strptime() 이용)
naljja = '2022-12-05 10:40:45'
print(type(naljja))
#1번 경우
mydate= datetime.strptime(naljja, '%Y-%m-%d %H:%M:%S')
#2번 경우
#mydate= datetime.datetime.strptime(naljja, '%Y-%m-%d %H:%M:%S')
print(mydate)
print(type(mydate))


