#public,private,protected

# class Employee():
#   workhours=18
#   def __init__(self,aname,asalary,arole):
#     self.name=aname
#     self.salary=asalary
#     self.role=arole
#   def emp(self):
#     return f"The name is {self.name} salary is {self.salary} and role is {self.role}"
#   @classmethod
#   def changedworkhours(cls,newtime):##cls will take the class of the object belongs to i.e mukilan object belong to which class.=>newtime is a argument which is passed to the class variable
#     cls.workhours=newtime

# mukilan=Employee("Mukilan",10000,"mcemployee")
# print(mukilan.workhours)###it is public ..here a workhours is accessed outside the class.

###################################################################################
# class Employee():
#   __workhours=18
#   def __init__(self,aname,asalary,arole):
#     self.name=aname
#     self.salary=asalary
#     self.role=arole
#   def emp(self):
#     return f"The name is {self.name} salary is {self.salary} and role is {self.role}"
#   @classmethod
#   def changedworkhours(cls,newtime):##cls will take the class of the object belongs to i.e mukilan object belong to which class.=>newtime is a argument which is passed to the class variable
#     cls.workhours=newtime

# mukilan=Employee("Mukilan",10000,"mcemployee")
# print(mukilan.__workhours)###it is private because no one should access it..here a workhours is accessed outside the class.so it wont work.therefore we hided the data
###by using the double underscore(__) before the variable name.
###################################################################################


# class Employee():
#   workhours=18
#   def __init__(self,aname,asalary,arole):
#     self.name=aname
#     self.salary=asalary
#     self.role=arole
#   def __emp(self):
#     return f"The name is {self.name} salary is {self.salary} and role is {self.role}"
#   @classmethod
#   def changedworkhours(cls,newtime):##cls will take the class of the object belongs to i.e mukilan object belong to which class.=>newtime is a argument which is passed to the class variable
#     cls.workhours=newtime

# mukilan=Employee("Mukilan",10000,"mcemployee")
# mukilan.__emp()###it is private because no one should access it..here a workhours is accessed outside the class.so it wont work.therefore we hided the data
# Employee.__emp()###it is private because no one should access it..here a workhours is accessed outside the class.so it wont work.therefore we hided the data

###########################################################################
# class Employee():
#   _workhours=18
#   def __init__(self,aname,asalary,arole):
#     self.name=aname
#     self.salary=asalary
#     self.role=arole
#   def emp(self):
#     return f"The name is {self.name} salary is {self.salary} and role is {self.role}"
#   @classmethod
#   def changedworkhours(cls,newtime):##cls will take the class of the object belongs to i.e mukilan object belong to which class.=>newtime is a argument which is passed to the class variable
#     cls.workhours=newtime

# mukilan=Employee("Mukilan",10000,"mcemployee")

# class Player(Employee):
#   pass
# newfunction=Player("bhuvi",100000,"bowler")
# print(newfunction._workhours)
# print(newfunction.__workhours)##it is double underscore so it is private so it wont work.
########it is protected which means the class varibles are acceessed in the derived class but not outside the class.(inherited ones)
###also if we use double underscore it is private so cant be accessed.if we want to access it use single underscore.then it can be accessed.

####################################################################################
#if we want to access the private,which is protected we are having one method called name mangling.

class Employee():
  __workhours=18
  def __init__(self,aname,asalary,arole):
    self.name=aname
    self.salary=asalary
    self.role=arole
  def emp(self):
    return f"The name is {self.name} salary is {self.salary} and role is {self.role}"
  @classmethod
  def changedworkhours(cls,newtime):##cls will take the class of the object belongs to i.e mukilan object belong to which class.=>newtime is a argument which is passed to the class variable
    cls.workhours=newtime

mukilan=Employee("Mukilan",10000,"mcemployee")
print(mukilan._Employee__workhours)###it is accessed by using the name mangling method.
#here we have to use the underscore and the class name before the variable name to access the private variable.