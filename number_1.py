import scipy.special as sp

# variant 6
# P(A)
p_a = sp.binom(10,4)/sp.binom(15,4)
print(p_a)
# P(B)
p_b = sp.binom(10,2)/sp.binom(15,3)
print(p_b)