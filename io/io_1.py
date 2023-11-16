# input
a = input()
print(a)

# 프롬프트를 띄워 사용자 입력받기
print(input("숫자를 입력하세요.\n>> ")) # input은 입력되는 모든 것을 문자열로 취급한다.

# print
print("life" "is" "too short") # 큰따옴표로 둘러싸인 문자열은 + 연산과 동일
print("life", "is", "too short") # 문자열 띄어쓰기는 쉼표로 한다

# 한 줄에 결괏값 출력하기
for i in range(10):
    print(i, end=" ") # end 매개변수를 생략 시 \n값이 들어가 줄바꿈이 수행된다