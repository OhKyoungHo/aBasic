# import mypackage.mymodule
# print('오늘의 날씨: ', mypackage.mymodule.get_weather())
# print('오늘은: ', mypackage.mymodule.get_date(), '요일입니다')

# 일부 함수만 가져오기
# from mypackage import mymodule
# print('오늘의 날씨: ', mymodule.get_weather())
# print('오늘은: ', mymodule.get_date(), '요일입니다')

# 일부 함수만 가져와서 별칭 붙이기
from mypackage import mymodule as mm
print('오늘의 날씨: ', mm.get_weather())
print('오늘은: ', mm.get_date(), '요일입니다')