# 리스트는 [], 튜플은 () 으로 생성
t1 = ()
t2 = (1, )
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

# 리스트와 차이점
    # 1가지 요소를 가질 때 ',' 를 반드시 붙여야함
    # 소괄호를 생략해도 됨 <-> 리스트는 반드시 [요소들] 형태로 대괄호 생략 불가능
    # * 리스트의 요소는 변경 가능하지만 튜플은 요소의 변경이 불가능함

t1 = (1, 2, 'a', 'b')
# del t1[0] -- 오류 TypeError: 'tuple' object doesn't support item deletion
# t1[0] = 'c' -- 오류 TypeError: 'tuple' object does not support item assignment

# 튜플 인덱싱
print(t1[0])
print(t1[3])

# 튜플 슬라이싱
print(t1[1:])

# 튜플 합치기
print(t1 + (3, 4))

# 튜플 곱하기
t2 = (3, 4)
print(t2 * 3)