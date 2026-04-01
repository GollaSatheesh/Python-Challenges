'''Add function helps to add individual elements to set. It only accepts single parameter'''
s=set()
s.add((10,20,23,23))#it accespts as single parameter , becuase inside bracket it considers only one object
print(s)
s.add(("Satheesh"))#it accepts strings also
print(s)
s.add(2.35)#It accepts float datatype also
print(s)
s.add(30)#As usual it accepts int datatype also , but accepts only single parameter
print(s)