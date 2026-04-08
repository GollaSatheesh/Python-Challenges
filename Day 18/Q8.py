def Factorial():
    num=int(input("Enter a Value : "))
    fact=1
    while num >=1:
        num=num*fact
        fact=fact+1
    for i in num(1,num-1):
        print(f"The factorial of the {num} is {i}")

Factorial()
