import tipovik_lib

tipovik_lib.event_happens_for_k1_to_k2_times(96,15,30,0.25)


p = 0.25
epsilon = 0.1
# n - ?
P = 0.9

F = tipovik_lib.inverse_laplace(0.45)
print(F /epsilon)
print((F/epsilon)**2 * 0.25*0.75)
