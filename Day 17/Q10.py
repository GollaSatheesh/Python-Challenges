l1=[1,2,3,4]
l2=["Satheesh","Madhu","Karthik","Chandu"]
d=dict(zip(l1,l2))
print(d)
for i in range(len(l1)):
    d[l1[i]]=l2[i]
