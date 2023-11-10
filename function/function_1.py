# 함수
"""
def 함수_이름(매개변수):
    수행할_문장1
    수행할_문장2

의 형태
"""


def add(a, b):
    return a + b

print(add(3, 4))


def say():
    return "Hi"

print(say())


def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a + b))

add(3, 4)
a = add(3, 4)
print(a) # None은 리턴값이 없다는 것

# 매개변수를 지정하여 호출하기
def sub(a, b):
    return a - b

print(sub(a=7, b=3))
print(sub(b=7, a=3))

# 여러 개의 잆력값을 받는 함수
# -> 입력값이 몇 개든 상관없이 입력값을 전부 모아 튜플로 만들어줌
# -> args는 임의의 변수이고 *변수 의 형태로 애스터리스크 뒤 아무 변수나 설정해도 됨. 다만 args는 arguments의 약자로 관례적으로 자주 사용함.
def add_many(*args):
    result = 0
    for i in args:
        result += i

    return result

print(add_many(1, 2, 3 ,4 , 5))

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i

    return result

print(add_mul("mul", 1, 2, 3, 4, 5))

# **kwargs
# -> 딕셔너리 타입으로 리턴해줌
# -> 이 또한 **변수명 형태로 사용 시 변수명과 상관없이 사용 가능하며 관례적으로 kwargs(Keyword Arguments) 를 사용함.
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)
