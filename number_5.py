
p_a1 = 1/6
p_a2 = 2/6
p_a3 = 3/6

p_b_a1 = 0.03
p_b_a2 = 0.02
p_b_a3 = 0.01

p_b = p_a1 * p_b_a1 + p_a2 * p_b_a2 + p_a3 * p_b_a3
print(p_b)

p_a1_b = p_b_a3 * p_a3/ p_b
print(p_a1_b)