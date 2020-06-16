p_circle = 0.8
p_square = 0.9
q_circle = 0.2
q_square = 0.1

p_c2 = p_square**2
print(p_c2)

q_c2 = 1 - p_c2
print(q_c2)

p_c1 = p_square * p_circle
print(p_c1)

q_c1 = 1 - p_c1
print(q_c1)

q_b2 = q_c1 * q_c2 * q_circle
print(q_b2)

p_b2 = 1 - q_b2
print(p_b2)

q_b1 = q_circle * q_square
print(q_b1)

p_b1 = 1-q_b1
print(p_b1)

p = p_b1 * p_square * p_b2
print(p)
