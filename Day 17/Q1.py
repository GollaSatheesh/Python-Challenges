'''Mini application using dictionary usecases are we can acces which element we want like 
keys and values or we want to acces key value pairs and it is a powerful data structure '''
n=int(input("Number of Vegetables :"))
v={}
for i in range(n):
    Vname=input("enter name :")
    Vprice=int(input("Enter price :"))
    v[Vname]=Vprice

print(v)
