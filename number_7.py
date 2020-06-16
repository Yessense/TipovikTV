import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
p1 = 0.3
p2 = 0.9

q1 = 1 - p1
q2 = 1 - p2

# 0
ksi_0 = q1 * q2
print(ksi_0)

# 1
ksi_1 = p1 * q2 + p2 * q1
print(ksi_1)

# 2
ksi_2 = p1 * p2
print(ksi_2)

x = [0, 1, 2]
prob = [ksi_0, ksi_1, ksi_2]

def display_graph(values:list, probability:list) -> None:
    import numpy as np
    import matplotlib.pyplot as plt
    x = np.array(values + [values[-1]+1])
    # Кумуятивная сумма

    values = np.array(probability)
    y = np.cumsum(values, dtype=float)
    fig, ax = plt.subplots()
    ax.set_facecolor('white')

    ax.hlines(y=y, xmin=x[:-1], xmax=x[1:], color='red', zorder=1)
    ax.vlines(x=x[1:-1], ymin=y[:-1], ymax=y[1:], color='red',
              linestyle='dashed', zorder=1)

    ax.scatter(x[0:-1], y, color='red', s=18, zorder=2)
    plt.ylabel('Probability')
    plt.xlabel('Xi')
    plt.title('График распределения случайной величины')
    ax.grid(False)
    ax.set_xlim(x[0], x[-1])

    plt.show()

def weighted_mean(values: list, weights: list) -> float:
    import numpy
    return np.average(values,weights=weights)

display_graph(x,prob)
print(f'Матожидание = {weighted_mean(x,prob)}')
print(f'Дисперсия = {weighted_mean(np.array(x)**2,prob) - weighted_mean(x,prob)**2}')


cum_prob = np.cumsum(np.array(prob))
print(cum_prob)

print()
