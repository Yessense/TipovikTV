
p_a1 = 0.4
p_a2 = 0.25
p_a3 = 0.35

p_b_a1 = 0.05
p_b_a2 = 0.06
p_b_a3 = 0.07

p_b = p_a1 * p_b_a1 + p_a2 * p_b_a2 + p_a3 * p_b_a3
print(p_b)

p_a1_b = p_b_a1 * p_a1/ p_b
p_a2_b = p_b_a2 * p_a2/ p_b
p_a3_b = p_b_a3 * p_a3/ p_b

print(" ответ: ", p_a1_b+ p_a2_b+ p_a3_b)

print(p_a1_b)