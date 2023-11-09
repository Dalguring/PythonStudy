# while 제어문
"""
while 조건문:
    수행할_문장1
    수행할_문장2

의 형태

자바와 같이 무한 루프를 방지하기 위한 변수값이 필요
"""
treeHit = 0

while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다")

# while문 탈출 (break)
coffee = 10
money = 300

while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# continue
a = 0

while a < 10:
    a += 1
    if a % 2 == 0: continue
    print(a)