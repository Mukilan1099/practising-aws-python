# keys=["a","b","c","d"]
# values=[1,2,3,4]
# dictcomp={k:v for k,v in zip(keys,values)}
# print(dictcomp)

############################################
# mydict1={x:x**2 for x in range(10)}
# print(mydict1)
############################################

# sdict={x.upper():x*3 for x in "mukilan"}
# print(sdict)

############################################
# conditiondict={x:x*2 for x in range(10) if x%2==0}
# print(conditiondict)
###########################################
l="MUKIL"
diction={x:{y:x+y for y in l} for x in l}
print(diction)