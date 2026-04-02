'''The diffrent mathematical operation we can performe on sets is union , intersection 
,difference and symmetric difference'''
a={1,2,3,4}
b={4,5,6,7}

#union
print(a|b,"And",a.union(b))

#Intersection
print(a&b,"and",a.intersection(b))

#Diffrence
print(a-b,"and",a.difference(b))

#Symmetric Difference
print(a^b,"and",a.symmetric_difference(b))
