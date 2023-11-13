# 함수의 리턴값은 언제나 하나이다
def add_and_mul(a, b):
    return a + b, a * b

"""
위와 같은 함수는 자바에서는 허용되지 않는다.
리턴값이 복수 개이기 때문인데, 파이썬에서도 리턴값은 하나여야 한다.
다만 파이썬은 위와 같은 형태일 때 튜플값으로 리턴한다.
"""

print(add_and_mul(3, 4))
# 또는 튜플 값을 분리해서 받고 싶다면 튜플 내 값의 수만큼 변수를 할당하면 된다.
result1, result2 = add_and_mul(3, 4)
print(result1)
print(result2)

# return 문을 통한 함수 종료
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다." % nick)

say_nick('야호')
say_nick('바보')

# 매개변수 초기값 미리 설정하기
def say_myself(name, age, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("서성민", 28)
say_myself("조민지", 27, False)

# 함수 내 변수의 효력 범위
a = 1
def vartest(a):
    a += 1

vartest(a)
print(a) # a = 1 <- 함수 내에서 사용하는 매개변수는 함수 안에서만 사용하는 지역변수. a 값에는 변함 없음

# 해결방법 1 : return 사용
a = 1
def vartest(a):
    a += 1
    return a

a = vartest(a)
print(a)

# 해결방법 2 : global 사용 / global a 는 함수 내에서 함수 밖의 a 변수를 직접 사용 하겠다는 뜻이다. 하지만 global 명령어는 사용하지 않는 것이 좋다(종속성) return 권장!
a = 1
def vartest():
    global a
    a += 1

vartest()
print(a)

# lambda 예약어 / 함수를 한 줄로 간결하게 만들 때 사용.
# 함수_이름 = lambda 매개변수1, 매개변수2, ... : 매개변수를_이용한_표현식 형태로 작성
add = lambda a, b: a + b
print(add(3, 4)) # lambda 함수는 return 명령어가 없어도 결괏값을 리턴함.