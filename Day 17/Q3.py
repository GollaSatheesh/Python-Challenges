
'''Nested collectoions means we creating tuple inside the dictionary'''
d={
    1:("One","two","three","Four","five"),
    2:("six","seven","seven","eight","Nine")
}
print(d)
for key,value in d.items():
    print(key,"-->",value)
