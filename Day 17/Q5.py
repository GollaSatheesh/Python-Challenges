#Merging of 2 lists
l1=[1,2,3,4,5,6]
l2=[1,2,3,4,5,6,7]
print(l1+l2)

#Merging of 2 tuples
v1=('one','two','three','four')
v2=(5,6,7,8,9,0,10)
print(v1+v2)

#For sets and dictionaries , we cant use "+" operator to merge collections we have to use "*" operator
#Merging of 2 sets
s1={1,"Apple",2,"banana",3,"Laptop"}
s2={"bag","bed","cupboard","Charger"}
print(*s1,*s2)
