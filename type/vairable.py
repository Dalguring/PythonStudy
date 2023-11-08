from copy import copy
# 변수
# 파이썬은 자바와 다르게 변수 타입을 설정할 필요 없이 스스로 자료형의 타입을 지정한다
a = [1, 2, 3]
print(id(a))
b = a
print(id(b))
# 주의 ! 자바에서는 b = a 형으로 변수 대입 시 변수값만 들어가지만 파이썬에서는 변수를 객체로 인식하여 같은 메모리 주소값을 가리키게 되고,
# 서로 같은 주소값을 가리키는 변수 중 하나를 수정하면 다른 변수의 값 또한 변경된다
a.append(4)
print(a)
print(b)
print(a is b)

# 같은 값을 가지면서 서로 다른 객체(서로 다른 주소를 가리키게 하는)를 생성하는 방법
# 1. [:] 이용하기
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

# 2. copy 모듈 이용하기
# from copy import copy 문으로 copy 모듈을 임포트
a = [1, 2, 3]
b = copy(a)

print(b is a)
a[1] = 4
print(a)
print(b)

# 변수를 만드는 여러가지 방법
a, b = ('python', 'life')
print(a)
print(type(a))
print(b)
print(type(b))

(a, b) = 'Python', 'lifee'
print(a)
print(type(a))
print(b)
print(type(b))

[a, b] = ['python', 'life']
print(a)
print(type(a))
print(b)
print(type(b))

a = 3
b = 5
a, b = b, a
print(a)
print(b)