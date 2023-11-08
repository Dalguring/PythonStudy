# if 문
"""
파이썬의 if문은
if 조건문:
    수행코드1
else:
    수행코드2

의 형태로 자바 및 다른 언어와 달리 :(콜론)으로 조건문이 끝났음을 암시하고, 들여쓰기를 통해 if 문 내부 동작임을 구분한다.
"""
money = True
if money:
    print("돈이 있다")
else:
    print("돈이 없다")

# and, or, not
money = 2000
card = True

if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

use = False
if not use: # 자바에서는 boolean 타입의 앞에 ! 를 붙여서 bool 값의 반전이 가능하지만, 파이썬에서는 not을 사용한다
    print("사용해라")
else:
    print("이미 사용했다")
    
# in, not in
# x (not) in 리스트, x (not) in 튜플, x (not) in 문자열 형태를 파이썬에서는 제공한다.
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# pass
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

# elif (else if와 같음)
pocket = ['paper', 'cellphone']
card = True
# elif를 사용하지 않았을 때
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("카드로 택시를 타고가라")
    else:
        print("걸어가라")

if 'money' in pocket:
    print("돈을 써서 택시를 타고가라")
elif card:
    print("카드로 택시를 타고가라")
else:
    print("걸어가라")

# 조건부 표현식
# 변수 = 조건문이_참인_경우의_값 if 조건문 else 조건문이_거짓인_경우의_값
score = 70
message = 'success' if score >= 60 else 'failure'
print(message)