Number=1000
def function2():
    Number=20
    print(f"The local number is {Number}")
    print(f"The global Number {globals()['Number']}")


function2()
