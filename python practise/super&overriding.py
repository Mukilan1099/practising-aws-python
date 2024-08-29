
# class A:
#   classvar1="I am a class variable in class A"
#   def __init__(self):
#     self.var1="I am inside class A's constructor"
#     self.classvar1="Instance variable in class A"

# class B(A):
#   classvar2="I am in class B"

# a=A()
# b=B()
# print(b.classvar1)

####whenever we are calling,first it will check the instance in the class which we are calling and check the instance variable in the class which we are calling.
### if it is not there then it will check the class variable in the class which we are calling and then it will check the class variable from which it inherits




######################################################
# class A:
#   classvar1="I am a class variable in class A"
#   def __init__(self):
#     self.var1="I am inside class A's constructor"
#     self.classvar1="Instance variable in class A"

# class B(A):
#   classvar2="I am in class B"
#   def __init__(self):
#       self.var1="I am inside class B's constructor"
#       self.classvar1="Instance variable in class B"
# a=A()
# b=B()
# print(b.classvar1)
####here Instance variable in class B is printed


#######################################################
# class A:
#   classvar1="I am a class variable in class A"
#   def __init__(self):
#     self.var1="I am inside class A's constructor"
#     self.classvar1="Instance variable in class A"

# class B(A):
#   classvar1="I am in class B"
#   def __init__(self):
#       self.var1="I am inside class B's constructor"
#       # self.classvar1="Instance variable in class B"
# a=A()
# b=B()
# print(b.classvar1)

#I am a class variable in class B=>it is printed.

#####here when u create the init constructor in bothe classes,parent,inherited,then the parent class wont allow to call the functions in the constructor.

############################################
# class A:
#   classvar1="I am a class variable in class A"
#   def __init__(self):
#     self.var1="I am inside class A's constructor"
#     self.classvar1="Instance variable in class A"

# class B(A):
#   # classvar1="I am in class B"
#   def __init__(self):
#       self.var1="I am inside class B's constructor"
#       # self.classvar1="Instance variable in class B"
# a=A()
# b=B()
# print(b.classvar1)


##it is printed:::I am a class variable in class A
#######################################################
# class A:
#   classvar1="I am a class variable in class A"
#   def __init__(self):
#     self.var1="I am inside class A's constructor"
#     self.classvar1="Instance variable in class A"
#     self.special="special"

# class B(A):
#   # classvar1="I am in class B"
#   def __init__(self):
#       self.var1="I am inside class B's constructor"
#       # self.classvar1="Instance variable in class B"
# a=A()
# b=B()
# print(b.special)
#####it wont work becaues the constructor is creates in the B so the A wont to call anything inside the constructor of A.
######################################################################
# class A:
#   classvar1="I am a class variable in class A"
#   def __init__(self):
#     self.var1="I am inside class A's constructor"
#     self.classvar1="Instance variable in class A"
#     self.special="special"

# class B(A):
#   # classvar1="I am in class B"
#   def __init__(self):
#       super().__init__()####this is used,so that the constructor of the parent class is accessed.
#       self.var1="I am inside class B's constructor"
#       # self.classvar1="Instance variable in class B"
# a=A()
# b=B()
# print(b.special)
# print(b.classvar1)
#special is printed.
##super().__init__() is used to access the constructor of the parent class and it denotes all th things in the constructor is pasted here.like that imagine .in such a way calling also occurs


################################################################
class A:
  classvar1="I am a class variable in class A"
  def __init__(self):
    self.var1="I am inside class A's constructor"
    self.classvar1="Instance variable in class A"
    self.special="special"

class B(A):
  # classvar1="I am in class B"
  def __init__(self):
      # super().__init__()#if it is pasted here means it means the below thing is pasted here.
      ####this is used,so that the constructor of the parent class is accessed.
      self.var1="I am inside class A's constructor"
      self.classvar1="Instance variable in class A"
      self.special="special"
      self.var1="I am inside class B's constructor"
      self.classvar1="Instance variable in class B"
a=A()
b=B()
print(b.special)
print(b.classvar1)
#it is printed Instance variable in class B because it iverrides the variable which created before.

#note:if super().__init__is pasted in the last line of constructor B ,then while printing the classvar1 it will print the class variable of class A.
