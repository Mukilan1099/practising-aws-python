# print(3+5)=>8
# print("3"+"5")=>35
#different forms =>polymorphism
#1.function overloading
#2.operator overloading
#3.method overloading
#4.method overriding
#5.function overriding
#6.operator overriding

#1.function overloading
# def add(a,b):
#   return a+b
# def add(a,b,c):
#   return a+b+c
# print(add(4,5,6))###it will show error because the function is overloaded.
#it will take the last function only.

#2.operator overloading
# class Employee():
#   def __init__(self,name,salary):
#     self.name=name
#     self.salary=salary
#   def __add__(self,other):###it is a operator overloading
#     return self.salary+other.salary
#   def __truediv__(self,other):
#     return self.salary/other.salary
#   def __sub__(self,other):
#     return self.salary-other.salary
#   def __mul__(self,other):
#     return self.salary*other.salary
# mukilan=Employee("mukilan",10000)
# hari=Employee("hari",20000)
# print(mukilan+hari)
# print(mukilan/hari)
# print(mukilan-hari)
# print(mukilan*hari)
# print(mukilan.__add__(hari))###it is a operator overloading
# print(mukilan.__truediv__(hari))
# print(mukilan.__sub__(hari))
# print(mukilan.__mul__(hari))


###same function in differnet classes=>different purposes
class A:
  def show(self):
    print("show of A")
class B():
  def show(self):
    print("show of B")
a=A()
b=B()
a.show()
b.show()

