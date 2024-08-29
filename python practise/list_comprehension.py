# list=[30,20,23,15]
# list1=[x for x in list if x%2==0]
# print(list1)

# list=['even number' if i%2==0 else "odd number" for i in range(10)]
# print(list)
##############################################################################
# lis=[num for num in range(100) if num%5==0 elif num%3==0]
# print(lis)
###it will fail because elif is not allowed in list comprehension
# lis=[num for num in range(100) if num%5==0 if num%3==0]
# print(lis)
###########################################################################
# words=("mukilan","hari","bhuvi")
# listwords=[strings[::-1] for strings in words]
# print(listwords)

##################################################################
# name=["m","v","l"]
# age=[23,24,25]
# # for name,age in zip(name,age):
# #     print(name,age)

# listzip=[(names,ages) for names,ages in zip(name,age)]
# print(listzip)
##################################################################
words=("mukilan","hari","bhuvi")
listwords=[len(word) for word in words]
print(listwords)