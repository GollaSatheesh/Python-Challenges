n=int(input("Number of Students :"))
v={}
for i in range(n):
    Vname=input("enter name :")
    Vprice=int(input("Enter Marks :"))
    v[Vname]=Vprice

for key,value in v.items():
    print(key,"->",value)
