a=[1,3,2,4,4,5]
b=[2,3,5,6]
c={2,3,5}
d=[11,12,13,14]
print(set(a))
a=set(a)
b=set(b)
print(a.union(b))
print(a.intersection(b))
print(a.issuperset(b))
print(c.issubset(b))
print(a.difference_update(b))
print(a)
print(d)
