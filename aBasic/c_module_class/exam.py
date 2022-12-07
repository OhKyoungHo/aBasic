
# 1번
from mypackage.exam.exmodule import deohagi
print(deohagi(3,4))

from mypackage.exam.exmodule import deohagi as plus

print(plus(3,4))
print(plus(3,'a'))

import mypackage
print(mypackage.exam.exmodule.deohagi(3,4))


'''
1. ③ 개별 .py 파일을 의미한다.
2. ➂ __init__.py
3. import fah_converter as fah
4. ➁ import os as *
5. from calculator import sum_func, minus_func, devide_func, multiply_func
'''