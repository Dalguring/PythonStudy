# 생성자
# class FourCal():
#     def add(self, first, second):
#         self.first = first
#         self.second = second
#
#         return self.first + self.second

# a = FourCal()
# a.add()
"""
Traceback (most recent call last):
  File "D:\PythonStudy\class\class_2.py", line 10, in <module>
    a.add()
TypeError: add() missing 2 required positional arguments: 'first' and 'second'
""" # 초기값 설정을 하지 않아 오류 발생

class FourCal():
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self, first, second):
        self.first = first
        self.second = second

        return self.first + self.second

a = FourCal(4, 2)
print(a.first)
print(a.second)
