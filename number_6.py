import scipy.special as scsp
import scipy.stats as scst

# import matplotlib.pyplot as plt
# data = scst.binom.rvs(n=5, p=0.25, size=1000)
# plt.hist(data)
# plt.show()

'''
a)
'''
# Схема Бернулли для n = 10, p = 0.3, k = 3
# Probability mass function at k of the given RV
p_exact_3 = scst.binom.pmf(n=10, p=0.3, k = 3)
print(p_exact_3)

# Куммулятивная функция распределения
p_less_than_1 = scst.binom.cdf(n=10,p=0.3,k=1)
print(p_less_than_1)

'''
b)
'''
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

#  Функция в точке
func = mlf(n=120,p=0.25,k=40)
print(func)

# тест
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


event_happens_for_k1_to_k2_times(n=120,k1=0,k2=1,p=0.25)

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

print(find_poisson_value(n=400,k=2,p = 0.015))

p_0 = find_poisson_value(n=400,k=0,p=0.015)
p_1 = find_poisson_value(n=400,k=1,p=0.015)

print(1 - round(p_0+p_1,4))