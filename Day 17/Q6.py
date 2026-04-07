'''For dictionries to merge we have to use "**" operator to merge one star isfor one key
and another star is for value'''
d1={
    1:"satheesh",
    2:"apple",
    3:"banana",
    4:"Apple"
}
d2={
    6:"volkwagen",
    7:"Cyberstar",
    8:"nano",
    9:"e vitara"
}
d3={**d1,**d2}
for key,values in d3.items():
    print(key,"->",values)
