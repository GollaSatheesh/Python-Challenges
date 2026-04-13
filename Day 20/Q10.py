from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,20000000,40000000]
result=reduce(lambda a,b:a if a>b else b,l)#a carries one after iterating in the list and compares it with b
print(result)
