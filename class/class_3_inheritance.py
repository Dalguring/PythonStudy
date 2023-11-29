# 상속
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal): # 클래스 상속을 위해서는 괄호 안에 상속할 부모 클래스 이름을 넣어주면 된다
    def pow(self):
        return self.first ** self.second

a = MoreFourCal(4, 2)
print(a.add()) # MoreFourCal 클래스는 부모 클래스인 FourCal의 메서드를 모두 상속 받음
print(a.pow())

# 메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
print(a.div())

# 클래스변수
class Family:
    lastname = '김'

print(Family.lastname)
a = Family()
b = Family()

print(a.lastname)
print(b.lastname)

Family.lastname = '박'
print(a.lastname) # 클래스 변수는 객체변수와 달리 클래스로 만든 모든 객체에 공유됨
print(b.lastname)

a.lastname = '최'
print(a.lastname)
print(Family.lastname)
print(b.lastname)