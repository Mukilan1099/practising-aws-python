# def dec(func):
#     def cloud():
#         print("cloud")
#         func()
#         print("technology")
#     return cloud
# def rator():
#     print("is booming")
    
# objee=dec(rator)
# objee()
###################################################
# class Employee():
#   def __init__(self,aname,asalary,arole):
#     self.name=aname
#     self.salary=asalary
#     self.role=arole
#   def emp(self):
#     return f"The name is {self.name} salary is {self.salary} and role is {self.role}"
  
# mukilan=Employee("Mukilan",10000,"mcemployee")
# #here we are passing the parameter to the object.So __init__ method is used.
# print(mukilan.emp())
###################################################
# class Employee():
    # workhours=18
#   def __init__(self,aname,asalary,arole):
#     
#     self.name=aname
#     self.salary=asalary
#     self.role=arole
#   def emp(self):
#     return f"The name is {self.name} salary is {self.salary} and role is {self.role}"
  
# mukilan=Employee("Mukilan",10000,"mcemployee")
# Employee.workhours=10
# #for changing the value of class variables  we can use this method.@classmethod
# print(mukilan.workhours)

####################################################
# class Employee():
#   workhours=18
#   def __init__(self,aname,asalary,arole):
#     self.name=aname
#     self.salary=asalary
#     self.role=arole
#   def emp(self):
#     return f"The name is {self.name} salary is {self.salary} and role is {self.role}"
#   @classmethod
#   def changedworkhours(cls,newtime):##cls will take the class of the object belongs to
#     cls.workhours=newtime

# mukilan=Employee("Mukilan",10000,"mcemployee")
# mukilan.changedworkhours(24)
# print(mukilan.workhours)


###############################################
#alternative constructor
# class Employee():
#   workhours=18
#   def __init__(self,aname,asalary,arole):
#     self.name=aname
#     self.salary=asalary
#     self.role=arole
#   def emp(self):
#     return f"The name is {self.name} salary is {self.salary} and role is {self.role}"
#   @classmethod
#   def changedworkhours(cls,newtime):
#     cls.workhours=newtime
#   @classmethod
#   def splitting(cls,string):
#     # return cls(*string.split("-"))
#     splitter=string.split("-")
#     return cls(splitter[0],splitter[1],splitter[2])

# mukilan=Employee("Mukilan",10000,"mcemployee")
# hari=Employee.splitting("hari-20000-AutomationEngineer")
# mukilan.changedworkhours(24)

# print(hari.salary)
# print(hari.emp())

############################################
 #static method is accesed only inside the class(employee)
class Employee():
  workhours=18
  def __init__(self,aname,asalary,arole):
    self.name=aname
    self.salary=asalary
    self.role=arole
  def emp(self):
    return f"The name is {self.name} salary is {self.salary} and role is {self.role}"
  @classmethod
  def changedworkhours(cls,newtime):
    cls.workhours=newtime
  @classmethod
  def splitting(cls,string):
    # return cls(*string.split("-"))
    splitter=string.split("-")
    return cls(splitter[0],splitter[1],splitter[2])
  
  @staticmethod
  def somestatic(string):
    print("This is static method",string)

mukilan=Employee("Mukilan",10000,"mcemployee")
hari=Employee.splitting("hari-20000-AutomationEngineer")
mukilan.changedworkhours(24)

print(hari.salary)
print(hari.emp())

print(Employee.somestatic("Written by mukil"))