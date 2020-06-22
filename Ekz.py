import numpy as np
from scipy import stats
# a = np.array([[1,2,-2,5],[2,0,2,3]])
# b = np.array([[1,-2],[2,4],[3,2],[0,1]])
# print(a @ b)

def find_h1h2h3_brak(H1: float, H2: float, H3: float,
                     p_A_H1: float, p_A_H2:float, p_A_H3:float,
                     rnd:int=3, ) -> None:
    '''
    Функция находит вероятность при случившимся событии А, что что это произошло на H?
    :param H1: Количество случаев H1
    :param H2: Количество случаев H2
    :param H3: Количество случаев H3
    :param p_A_H1: Вероятность события А при Н1
    :param p_A_H2: Вероятность события А при Н2
    :param p_A_H3: Вероятность события А при Н3
    :param rnd: Количество знаков для округления
    '''
    quantity = H1 + H2 + H3
    p_H1 = H1/quantity
    p_H2 = H2/quantity
    p_H3 = H3/quantity

    p_A = p_H1 * p_A_H1 + p_H2 * p_A_H2 + p_H3 * p_A_H3

    p_H1_A = p_A_H1 * p_H1 / p_A
    p_H2_A = p_A_H2 * p_H2 / p_A
    p_H3_A = p_A_H3 * p_H3 / p_A

    print(f"Вероятность что произойдет событие событие А = {round(p_A,rnd)}\n")

    print(f"Вероятность что событие А произошло при условии H1 = {round(p_H1_A,rnd)}")
    print(f"Вероятность что событие А произошло при условии H2 = {round(p_H2_A,rnd)}")
    print(f"Вероятность что событие А произошло при условии H3 = {round(p_H3_A,rnd)}\n")

    print(f"Проверка. Сумма H1 + H2 + H3 = {p_H1_A+p_H2_A+p_H3_A}")



# find_h1h2h3_brak(40,25,35,0.05,0.06,0.07,3)

def check_p_for_limited_geom_dist(p,k):
    '''
    Вероятность в геометрическом распределении встретить результат в первых К случаях
    :param p: Вероятность события
    :param k: Количество случаев
    :return: Вероятность
    '''
    sum = 0
    probability = 0.3
    for i in range(4):
        sum += (1-probability)**(i) * probability
    print(f'Вероятность события в первых к случаях = {round(sum,4)}')
    return sum

# print(1-check_p_for_limited_geom_dist(0.3,4))

def find_несмещенная_выборочная_дисперсия_и_все_прочее(xi,mi):

    xarr = np.array(xi)
    marr = np.array(mi)

    data = np.repeat(xi,mi)

    print(f'Выборочное среднее = {data.mean()}')
    print(f'Мода = {stats.mode(data)[0][0]}')
    print(f'Дисперсия = {data.var()}')
    print(f'Несмещенная выборочная дисперсия = {data.var(ddof=1)}')
    print(f'Среднеквадратичное отклонение = {data.std()}')
    print(f'Несмещенное среднеквадратичное отклонение = {data.std(ddof=1)}')

p_less_than_1 = stats.binom.cdf(n=10,p=0.04,k=1)

print(1-p_less_than_1)
# find_несмещенная_выборочная_дисперсия_и_все_прочее([3.5,4.1,4.7,5.4,5.6,6.2],[2,3,2,4,3,2])
