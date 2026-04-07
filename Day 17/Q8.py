d={
    1:{"Name":"Satheeesh","class":"12","Marks":"100"},
    2:{"Name":"Madhu","Class":"12","Marks":"99"}
}
for name,info in d.items():
    print(f"{name}")
    for key,value in info.items():
        print(key,"->",value )
