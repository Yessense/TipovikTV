p1 = 0.5
p2 = 0.4
p3 = 0.3

q1 = 1-p1
q2 = 1-p2
q3 = 1-p3

print(p1*q2*q2*q3*q3 + q1*p1*q2*q2*q3*q3 + q1*q1*p2*q3*q3+
      q1*q1*q2*p2*q3*q3+ q1*q1*q2*q2*p3+ q1*q1*q2*q2*q3*p3)
