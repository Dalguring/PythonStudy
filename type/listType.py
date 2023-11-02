# 리스트 생성
odd = [1, 3, 5, 7, 9]
print(odd)

# 이중리스트 생성
a = [1, 2, ['Life', 'is']]
print(a)

# 리스트 인덱싱
print(a[2])
print(a[2][0])
print(odd[0] + odd[1])
print(odd[-1])

# 리스트 슬라이싱
print(odd[0:2])
b = odd[:3]
print(b)
print(a[2][:2])

# 리스트 더하기
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)

# 리스트 반복하기
print(a * 2)

# 리스트 길이 구하기
print(len(a))

# 리스트 연산 오류
# print(a[0] + 'hi') -- int형과 str형은 더할 수 없음
print(str(a[0]) + 'hi')

# 리스트 수정하기
a = [1, 2, 3]
a[2] = 4
print(a)

# del 함수를 통해 리스트 요소 삭제하기
del a[1]
print(a)

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

print("=" * 50)
print("[ 리스트 함수 ]\n")

# 리스트 관련 함수
# append

a = [1, 2, 3]
a.append(4)
print(a)

a.append([5, 6])
print(a)

# sort
b = [1, 4, 3, 2]
b.sort()
print(b)

b = ['a', 'c', 'b']
b.sort()
print(b)

# reverse
b.reverse()
print(b)

# index
a = [1, 2, 3]
print(a.index(3))
# print(a.index(0)) -- 존재하지 않는 요소를 index 함수에 전달 시 오류 발생

# insert
a = [1, 2, 3]
a.insert(0, 4)
print(a)

a.insert(3, 5)
print(a)

# remove -- remove() 함수에 전달된 파라미터 값을 찾아 첫 번째 요소를 삭제
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)
a.remove(3)
print(a)

# pop
a = [1, 2, 3]
print(a.pop())
print(a)

a = [1, 2, 3]
print(a.pop(1))
print(a)

# count
a = [1, 2, 3, 1]
print(a.count(1))

# extend -- 파라미터로 리스트만 올 수 있음
a = [1, 2, 3]
a.extend([4, 5])
print(a)

b = [6, 7]
a.extend(b)
print(a)

