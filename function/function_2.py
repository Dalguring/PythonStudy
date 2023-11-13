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