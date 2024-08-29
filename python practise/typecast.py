# numbers=["33","44","55","80"]
# print(type(numbers))
# for i in range(len(numbers)):
#   numbers[i]=int(numbers[i])
# print(type(numbers[0]))


###using map()
# numbers=["33","44","55","80"]
# numbers=list(map(int,numbers))##list must be put before map,=>int refers that int function is used in all the elements of the list.
# print(numbers[0])

#####using 
# def square(a):
#   return a*a

# num=[1,2,3,4,5]
# for i in num:
#   print(square(i))

# num=list(map(square,num))####it is also used.

  #####using lambda
# num=[1,2,3,4,5]
# num=list(map(lambda x:x*x,num))
# print(num)
# for i in num:
#   print(i)

####filter()method
# def greater(a):
#   return a>5
# list1=[1,2,3,4,5,6,7,8,9]

# list1=list(filter(greater,list1))
# print(list1)

#######################
#using reduce()
from functools import reduce
list1=[1,2,3,4]
num=reduce(lambda x,y:x+y,list1)####cumulative addition
print(num)
