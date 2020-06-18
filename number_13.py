from scipy.special import ndtri

p = 0.95
epsilon = 0.5
mean = 0


from statistics import NormalDist
def inverse_laplace(x:float) -> float:
    from statistics import NormalDist
    print(f'Обратное значение функции Лапласа при x={x} равно {round(NormalDist().inv_cdf(x + 0.5),2)}')
    return NormalDist().inv_cdf(x + 0.5)

x = inverse_laplace(p/2)

sigma = epsilon/x
print(f'Sigma = {round(sigma,4)}')