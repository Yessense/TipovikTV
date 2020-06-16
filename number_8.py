import scipy.stats as scst
import tipovik_lib
n = 10
p = 0.75
m = 1
q = 1 - p

# Часть 1
p_exact_0 = scst.binom.pmf(n=10, p=0.75, k = 0)
print(round(p_exact_0,4))

p_exact_1 = scst.binom.pmf(n=10, p=0.75, k = 1)
print(round(p_exact_1,4))

# Часть 2
tipovik_lib.find_poisson_value(n=550,k=5,p=0.01)
