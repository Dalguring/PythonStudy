# 문자열 타입
# 파이썬의 문자열은 변경 불가능한 자료형임
# "", '', """, '''
print("[ 문자열 출력 ]\n")

print("Hello World")
print('Python is fun')
print("""Life is too short, You need python""")
print('''Life is too short, You need python''')

print("=" * 50)

# ""나 ''로도 문자열 타입을 생성할 수 있지만, 멀티라인을 입력하거나 문자열 내 " 나 '를 문자열 선언형으로 인식하지 않도록 """ , ''' 를 사용할 수 있다.
print("""my friend said, "welcome to python world" """)
print('''It's mine''')

multiline = """Life is too short
You need python"""

print(multiline)

# """ 이후 줄바꿈(엔터 입력) 시 표시 되는 문자열 또한 줄이 바뀐 문자열이 표시됨
multiline = """
Life is too short
You need python
"""

print(multiline)

print("=" * 50)

# 작은 따옴표 내 큰 따옴표, 큰 따옴표 내 작은 따옴표는 문자열로 인식된다 (이스케이프 코드를 이용해서도 표현 가능)
print("Python's favorite food is perl")
print('"Python is very easy." he says')

print("=" * 50)
print("[ 문자열 연산 ]\n")
# 문자열 연산
head = "Python"
tail = ' is fun!'

print(head + tail)

a = 'python'
print(a * 2)

print("=" * 50)
print("[ 문자열 길이 ]\n")

# 문자열 길이(공백도 포함됨)
a = "Life is too short"
print(len(a))

a = "Life is too short "
print(len(a))

# 문자열 인덱싱
print(a[3])

if a[-1] == ' ':
    print("공백문자열")
else:
    print(a[-1])

print("=" * 50)
print("[ 문자열 인덱싱과 슬라이싱 ]\n")

# 문자열 슬라이싱
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]

print(b)
print(a[0:4])
print(a[5:])
print(a[:17])
print(a[19:-7])

print("=" * 50)
print("[ 문자열 포매팅 ]\n")

# 문자열 포매팅
print("I eat %s apples" % 3)
print("I eat %s apples" % "five")
print("I ate %d apples. So I was sick for %s days." % (10, "five"))
print("Error is %d%%" % 98)

# 정렬과 공백
print("%10sJane" % "hi")
print("%-10sJane" % "hi")
print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))

# 소수점 표현
print("%0.4f" % 3.42134234)

# format 함수를 이용한 문자열 포맷
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))
print("I ate {0} apples. So I was sick for {1} days".format(10, "three"))
print("I ate {number} apples. So I was sick for {day} days".format(number=10, day=3))
print("I ate {0} apples. So I was sick for {day} days".format(10, day=3))
print("{{ and }}".format()) # {}와 같은 중괄호 문자는 포매팅을 위한 문자이므로 연속해서 사용 시 표시됨

# f 문자열 포매팅
name = "서성민"
print(f"나의 이름은 {name} 입니다.")
print(f"{'hi':>10}")

print("=" * 50)
print("[ 문자열 함수 ]\n")

# count 함수
a = "hobby"
print(a.count("b"))

# find 함수
a = "Python is the best choice"
print(a.find("b"))
print(a.find("k"))

# index 함수
a = "Life is too short"
print(a.index('t'))
    # print(a.index('k')) -- index 함수는 찾을 대상이 문자열에 존재하지 않는다면 오류를 발생시킴

# join 함수
print(",".join('abcd'))

# upper 함수
print("hi".upper())
a = "hI bYe"
print(a.upper())

# lower 함수
print(a.lower())

# lstrip, rstrip, strip 함수
a = "{0:^5}".format("hi")
print(a.lstrip())
print(a.rstrip())
print(a.strip())

# replace 함수
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# split 함수 -- 리스트 형으로 리턴
a = "Life is too short"
print(a.split())
b = "a:b:c:d"
print(b.split(":"))