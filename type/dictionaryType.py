# 딕셔너리 자료형
# 자바의 Map과 같이 Key와 Value의 대응관계로 이루어진 해시 자료형

dic = {'name' : 'pey', 'phone' : '010-9999-9999', 'birth' : '1118'}
print(dic.get('name'))

# value값에 리스트도 넣을 수 있음
a = {'a' : [1, 2, 3]}
print(a.get('a'))

# 딕셔너리 Key, Value 쌍 추가하기 -- 주의! 대괄호 안에 들어가는 숫자는 인덱스가 아니고 Key 값임
a = {1: 'a'}
a[2] = 'b'
print(a)
a['name'] = 'pey'
print(a)
a[3] = [1, 2, 3]
print(a)

# 딕셔너리 요소 삭제하기
print(a)
del a[1]
print(a)

# 딕셔너리 사용
grade = {'pey': 10, 'julliet': 90}
print(grade['pey'])
print(grade['julliet'])

# 딕셔너리 선언 시 리스트는 key값이 될 수 없지만 튜플은 key값이 될 수 있다
# a = {[1, 2] : 'hi'} -- TypeError: unhashable type: 'list'
a = {(1, 2) : 'hi'}
print(a)

# 딕셔너리 함수
# keys()
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys()) # keys()함수의 리턴 타입은 dict_keys 객체인데, 리스트로 변환하지 않더라도 반복구문에서 사용 가능하다
print(list(a.keys())) # 리스트 형으로 변환하여 사용도 가능하다

# values()
print(a.values())

# items()
print(a.items())

# clear()
a.clear()
print(a)

# get()
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('name'))
print(a.get('nokey')) # None 리턴
print(a.get('nokey', '해당 key값이 없을 경우 return'))

# in()
print('name' in a)
print('nokey' in a)