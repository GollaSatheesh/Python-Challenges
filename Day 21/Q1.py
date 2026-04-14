'''Funtionc aliasing in python is definining the function to the new variable , 
Because the functions re objects in the python'''
def hello(name):
    print(f"{name} Good Evening")

result=hello
print(result("Satheesh"))
