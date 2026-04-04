'''Dictionary is collection of items which stores the in formate of keys and values ,
  if we want to access keys there is inbuilt method called "DictionaryName.keys()" and
  if we want to access values same like keys ,"DictionaryName.values()" and if we want
  access keys and values (They are also called items) want to acces them "DictionaryName.items()"
  '''
d={
    "Name":"Satheesh",
    "Pursuing":"Data scientist"
   }
print("The values in the Dictionary:",d.values())
print("The keys in the Dictionary:",d.keys())
print("The items in the Dict:",d.items())

for keys,values in d.items():
        print(keys,"->",values)
