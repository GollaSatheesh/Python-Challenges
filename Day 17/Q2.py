'''Merging of collections means adding two dictionaries into one or , lists,tuples and sets .
This is called merging of two collections'''

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

#Merging of 2 dictionaries
#If we have to merge 2 dictionaries we have to use "**" operator
d1={
    1:"Satheesh",
    2:"Sameer",
    3:"Karthik",
    4:"chandu"
}
d2={
    5:"Ram charan",
    6:"Lingesh",
    7:"ram linga"
}
d3={**d1,**d2}
print(d3)
