# 파일을 통한 입출력
f = open("새파일.txt", 'w')
f.close()
# 수행 시 위 코드를 실행한 디렉토리 내 새로운 파일이 생성됨
# 파일_객체 = open(파일_이름, 파일_열기_모드)
# r : 읽기 모드 / w : 쓰기 모드 / a : 추가 모드
# w -> 해당 파일이 존재할 경우 원래 내용이 사라짐, 파일이 존재하지 않을 경우 새로운 파일이 생성됨
f = open("D:/PythonStudy/새파일.txt", 'w') # 파일 명 앞에 경로 지정 시 해당 경로에 해당 파일 명을 가진 파일이 생성됨 -> '/'를 사용하거나 '\\'를 사용 또는 r"D:\~"의 형태로 사용 가능함.
f.close()

# 쓰기 모드로 열어 내용 쓰기
f = open(r"D:\PythonStudy\새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)

f.close()

# readline()
f = open("D:\\PythonStudy\\새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)

f.close()

# readlines() -> 모든 줄을 읽어서 각각의 줄을 요소로 가지는 리스트를 리턴해줌.
f = open(r"D:\PythonStudy\새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line.rstrip())

f.close()

print()

# read() -> 파일의 내용 전체를 문자열로 리턴함
f = open(r"D:\PythonStudy\새파일.txt", 'r')
data = f.read()
print(data)
f.close()

# for문을 통하여 읽기
print("====for문====")
f = open(r"D:\PythonStudy\새파일.txt", 'r')
for line in f:
    print(line.rstrip())

f.close()

# 파일에 새로운 내용 추가하기
f = open(r"D:\PythonStudy\새파일.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)

f.close()

# with 문과 함께 사용하기 -> with문을 사용하면 파일을 열고 닫은 것을 자동으로 처리할 수 있다
# ->  with문을 벗어나는 순간 열린 파일 객체 f가 자동으로 닫힌다.
with open("foo.txt", 'w') as f:
    f.write("Life is too short, you need python")