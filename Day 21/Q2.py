'''A nested function is nothing but defining the function inside the it is called Nested function'''
def Outer():
    print("I am outer")
    def inner():
        print("I am inner")

    inner()
result=Outer()