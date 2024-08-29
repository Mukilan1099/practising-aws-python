class Employee:
  workhours=18
  pass
mukil=Employee()
hari=Employee()
mukil.name="mukilan"
mukil.salary=10000########all are instance variables
mukil.role="mcemployee"

hari.name="haribhuvi"
hari.salary=200000
hari.role="AutomationEngineer"####instance variables
#class variables can be used by all the objects,but cant change it
print(mukil.workhours)##object/instance can access the class variables.but it cant change the class variables 
hari.workhours=24##this will create a new instance variable for hari object.....it creates a new variable but it doesnt change the class variable
print(hari.workhours)
print(Employee.__dict__)  ##it will show the class variables###when it is printed we can see the workinghours  is not changed in the class variables