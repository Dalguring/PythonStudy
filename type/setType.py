# 집합 자료형

s1 = set([1, 2, 3])
print(s1)

s2 = set("Hello")
print(s2)

emptySet = set()
print(emptySet)

# 집합 자료형의 특징
"""
중복을 허용하지 않는다.
순서가 없다.
인덱싱을 통해 요솟값을 얻을 수 없다 -> 리스트나 튜플형으로 변환 후 접근 가능
"""

s1 = set([1, 2, 3])
l1 = list(s1)
print(l1)
print(l1[0])

t1 = tuple(s1)
print(t1)
print(t1[0])

# 교집합, 합집합, 차집합
s1 = set([1, 2, 3, 4, 5 ,6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1 & s2)
print(s1.intersection(s2))

# 합집합
print(s1 | s2)
print(s1.union(s2))

# 차집합
print(s1 - s2)
print(s1.difference(s2))

# 집합 관련 함수
# add
s1 = {1, 2, 3}
s1.add(4)
print(s1)

# update
s1.update([4, 5, 6])
print(s1)

# remove
s1.remove(2)
print(s1)