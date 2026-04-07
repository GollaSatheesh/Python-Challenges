'''Merging and printing different types of collections'''
#merging list and tuple
l=[1,2,3,4,5,6]
t=(7,8,9,10,11)
print(*l,*t)

#Merging dictionary and set
s={1,23,24,25,2,7,18}
d={
    "11":"Satheesh",
    "12":"Laptop",
    "13":"Bag"
}
result=list(s)+list(d.items())
print(result)
