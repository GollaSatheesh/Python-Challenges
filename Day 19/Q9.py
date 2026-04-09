#use of global variabe inside the function
value=20
def function1():
    global value #this value for this varibale will be global after using the keyword
    value=100 # This value becomes the global
    print(value)

function1()
