'''using Set default method if we searched the key which is not in the dictionary
it adds key with value with default none if you given value it adds so it wont raises
error'''
 
Details={
            "Name":"Mahesh",
            "Place":"Bangalore",
            'age':22
 }

Details.setdefault("city",)#Here default value stores with none
print(Details)
