from math import e

n = 1000
p = 0.002

alpha = n*p # 2.0
print(alpha)

p0 = e**-2
print(p0)

p1 = 2*e**-2
print(p1)

p2 = 2*e**-2
print(p2)

print(p0+p1+p2)

p = 1 - (p0+p1+p2)
print(p)
