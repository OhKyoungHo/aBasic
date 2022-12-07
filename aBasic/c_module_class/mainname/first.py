print('first 모듈 시작')
print('first.py __name__:', __name__)    # __name__ 변수 출력
print('first 모듈 끝')


'''
#여기서 사용하면 메인의 모듈로 이름이 바뀜
#즉 first에서 할떄는 그냥 내자신이니 first께 그대로 진행이되지만
#여기 second에서는 돌리면  second.py __name__: __main__ 이렇게나옴
#왜냐 second이 내꺼 임포트 했자나 !
print('second.py __name__:', __name__)  # __name__ 변

즉, first에서 출력하면 해당 __name__이 __main__으로 나옴
but, second에서 출력하면 first의 __name__이 first로 나옴(second에서 import했기 때문)
second에서 자기 자신의 __name__은 __main__으로 나옴

즉, 자신의 파일에서 __name__으로 하면 __main__으로 나옴
but  다른  파일이  해당 파일을 import 한 경우는 import한 파일에서는 __name__이 자신의 파일 이름으로 나온다


'''