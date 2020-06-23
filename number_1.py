import scipy.special as sp

# variant 6
# P(A)
# p_a = sp.binom(10,4)/sp.binom(15,4)
# print(p_a)
# P(B)
# p_b = sp.binom(10,2)/sp.binom(15,3)
# print(p_b)

a1 = sp.binom(5,2)*sp.binom(5,1)*sp.binom(2,1)*sp.binom(3,1)
a2 = sp.binom(5,2)*sp.binom(5,1)*sp.binom(2,2)

b = sp.binom(15,5)
print(a1,a2,b)


p = (a1+a2)/b
print(p)
