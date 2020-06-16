def mlf(n:int,p:float, k: int) -> float:
    '''
    :param n: Общее количество событий
    :param p: Вероятность успешного события
    :param k: Прозойдет в точности k событий
    :return: Вероятность происхождения в точности k событий по форму Муавра Лапласа.
    '''
    denominator = (n * p * (1-p)) ** 0.5
    argument = (k - n * p) / denominator
    func = phi(argument)
    result = 1/denominator * func
    return result

def phi(x:float) -> float:
    '''
    :param x: Переменная х
    :return: Значение по формуле Муавра-Лапласа для х
    '''
    import math
    return 1 / (math.sqrt(2 * math.pi)) * math.e ** (-(x ** 2) / 2)

def event_happens_for_k1_to_k2_times(n:int,k1:int,k2:int,p:float) ->float:
    q = 1-p
    import scipy
    arg2 = (k2 - n * p) / (n * p * q) ** 0.5
    arg1 = (k1 - n * p) / (n * p * q) ** 0.5
    print("---------------")
    print(f'Calculating event happens ({k1} <= x <= {k2} times')
    print(f'1. k2 - n*p = {k2-n*p}')
    print(f'2. k1 - n*p = {k1 - n * p}')
    print(f'3. sqrt(npq) = {round((n*p*q)**0.5,4)}')
    print(f'4. F({round(arg2,4)}) - F({round(arg1,4)})')
    cdf_k2 = scipy.stats.norm.cdf(arg2) - 0.5
    cdf_k1 = scipy.stats.norm.cdf(arg1) - 0.5
    print(f'5. {round(cdf_k2,4)} - {round(cdf_k1,4)}')
    print(f'6. Result = {round(cdf_k2-cdf_k1,4)}')
    print("---------------")
    return cdf_k2-cdf_k1

def find_poisson_value(n: int, k: int, p:float) ->float:
    import scipy
    import math
    from scipy.special import factorial
    mu = n*p
    print("---------------")
    print(f"Calculating event happens {k} times from {n}")
    print(f'1. Матожидание = n*p = {n*p}')
    print(f'2. Mu**k = {mu**k}')
    print(f'3. Факториал k! = {factorial(k)}')
    print(f'4. Mu**k/k! = {mu**k/factorial(k)}')
    print(f'5. e**(-mu) = {round(math.e**(-mu),4)}')
    print(f'6. Mu**k/k!*e**-mu = {round(mu**k/factorial(k)*math.e**(-mu),4)}')
    print(f'Result = {round(scipy.stats.poisson.pmf(k=k,mu=mu),4)}')
    print("---------------")
    return scipy.stats.poisson.pmf(k=k,mu=mu)

def weighted_mean(values: list, weights: list) -> float:
    import numpy
    return np.average(values,weights=weights)


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


def geom_distribution(n: int, p: float) -> float:
    '''
    Верояность того, что событие случится в n попытках
    :param n:  количество попыток
    :param p: вероятность останавливающего события
    :return: вероятность
    '''
    print("---------------")
    summ = 0
    for i in range(n):
        temp = (1 - p) ** (i) * p
        print(f'{i+1}. {round(1 - p,4)}^{i} * {p} = {round(temp,4)}')
        summ += temp
    print(f'Сумма значений = {round(summ,4)}')
    print("---------------")
    return summ


def geom_average(p: float) -> float:
    print("---------------")
    print(f'Мат. ожидание для вероятности p = {round(1/p,4)}')
    print("---------------")
    return 1 / p


def geom_dispersion(p: float) -> float:
    print("---------------")
    print(f'Дисперсия для вероятности p = {round((1 - p) / p ** 2,4)}')
    print("---------------")
    return (1 - p) / p ** 2

