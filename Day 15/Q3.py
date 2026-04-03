'''There are few types to delete elements in the dictionary , first one is del DictName[key] command this deletes the value associated with this key value
and second method is pop.item(), this deletes the item present in the last row,and pop(), this also deletes
the value associated with key , and another method is to clear all elements in the dictionary ,clear(DictionaryName)'''


d={'name':'satheesh','age':23,'city':'bangalore','Seeking':'Data scientist'}

del d['name']
print(d)

d.popitem()
print(d)

d.pop('age')
print(d)

d.clear()
print(d)

del d; #it deletes entire dictionary 
print(d)
