# Class란 똑같은 무언가를 계속 만들어 낼 수 있는 설계 도면(틀), 객체(Object)는 클래스로 만든 피조물(틀로 찍어 낸 것)
class Cookie:
    pass

a = Cookie()
b = Cookie() # 아무 기능이 없는 Cookie 클래스지만 객체를 무한으로 생성할 수 있다
# a = Cookie()에서 a는 Cookie의 인스턴스이고 a 는 객체이다
"""
설계
a = FourCal()
a.setdata(4, 2)
a.add()
a.mul()
a.sub()
a.div()
이 동작 가능하도록 FourCal 클래스 생성
"""

class FourCal:
    def setdata(self, first, second):
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

a = FourCal()
print(type(a)) #<class '__main__.FourCal'>
print(a.setdata(4, 2)) # setdata 메서드에는 파라미터가 3개인데, 이 때 self는 a 객체가 전달된다
print(a.first)
print(a.second)

a = FourCal()
b = FourCal()

a.setdata(4, 2)
b.setdata(3, 7)

print(a.add())
print(b.add())
print(a.mul())
print(a.sub())
print(a.div())