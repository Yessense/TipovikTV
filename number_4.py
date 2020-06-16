# Вероятности работы
p1 = 0.6
p2 = 0.5
p3 = 0.7
# Вероятности отказа
q1 = 1 - p1
q2 = 1 - p2
q3 = 1 - p3


p4 = q4 = 0.5

p = p1* p2 * p3
print(p)

p1_doubled = 1 - q1*q4
p2_doubled = 1 - q2*q4
p3_doubled = 1 - q3*q4

print(p1_doubled,p2_doubled,p3_doubled)

p_doubled  = p1_doubled* p2_doubled* p3_doubled
print(p_doubled)

result = p_doubled/p
print(result)