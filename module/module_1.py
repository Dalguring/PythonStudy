# 파이썬에서 모듈은 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일을 말한다
import mod1
print(mod1.add(3, 4)) # 위와 같이 import 모듈명 으로 선언 시 해당 모듈 내의 함수나 변수를 사용하려면 모듈명.함수명으로 접근해야함

from mod1 import sub
print(sub(5, 2)) # 위와 같이 from 모듈명 import 함수명 으로 선언 시 함수명만으로 사용이 가능하다

# from mod1 import * <- 해당 모듈 내의 모든 함수를 import
print(mod1.__name__) # __name__ 변수는 파이썬 내부적으로 자신의 파일일 경우 __main__값이 저장되며 타 모듈에서 import 할 경우 해당 모듈의 이름이 저장된다