a={a for a in range(10)}
b={b for b in range(6)}
print(a|b,"and",a.union(b))
print(a&b,"and",a.intersection(b))