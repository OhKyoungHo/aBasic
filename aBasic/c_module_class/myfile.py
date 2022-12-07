#import mymodule
# 모듈 전체를 참조할 수 있다.

# 방법1(import 해서 변수 선언해서 함수 호출 )
# weather = mymodule.get_weather()
# today = mymodule.get_date()
# print('오늘의 날씨: ', weather)
# print('오늘은: ', today,'요일입니다' )

# 방법2(import 해서 변수선언 없이 함수 호출)
# print('오늘의 날씨: ', mymodule.get_weather())
# print('오늘은: ', mymodule.get_date(),'요일입니다' )

# 방법 3(import하고 별칭으로 부여해서 함수 호출)
# import mymodule as mm
# print('오늘의 날씨: ', mm.get_weather())
# print('오늘은: ', mm.get_date(), '요일입니다')

# 방법 4(모듈에서 필요한 부분만 import해서 함수 호출)
from mypackage.mymodule import get_weather, get_date
print('오늘의 날씨: ', get_weather())
print('오늘은: ', get_date(), '요일입니다')

