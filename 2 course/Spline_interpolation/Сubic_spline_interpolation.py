# Интерполяция кубическими сплайнами методом прогонки

import matplotlib.pyplot as plt
import numpy as np

def Splines(interpDots, x, y):
    """
    Вычислить значения сплайнов.
    
    Входные данные:
    interpDots - одномерный массив точек ОХ, в которых вычисляются значения сплайнов
    x - одномерный массив, интервал, на котором происходит интерполяция
    y - одномерный массив, значения функции в точках массива x
    
    Возвращает список(сплайны), по значениям которых строится интерполируемая функция.
    
    """
    
    n = len(x)

    h = np.zeros(n)
    for i in range(1, n):
        h[i] = x[i] - x[i-1]

    g = np.zeros(n)
    for i in range(1, n - 1):
        g[i] = 3*(y[i+1] - y[i])/h[i+1] - 3*(y[i] - y[i-1])/h[i]

    alpha = np.zeros(n)
    alpha[2] = -1/2*h[2]/(h[1] + h[2])
    for i in range(3, n - 1):
        alpha[i] = (-1*h[i] - alpha[i-1]*h[i-1])/(2*(h[i-1] + h[i]))
    alpha[n - 1] = 0

    beta = np.zeros(n)
    beta[2] = g[1] / (2*(h[1] + h[2]))
    for i in range(3, n):
        beta[i] = (g[i-1] - beta[i-1]*h[i-1]) / (2*(h[i-1] + h[i]))

    c = np.zeros(n + 1)
    for i in range(n - 1, 1, -1):
        c[i] = alpha[i]*c[i+1] + beta[i]
    c[1] = 0

    a = np.zeros(n)
    b = np.zeros(n)
    d = np.zeros(n)
    for i in range(1, n):
        a[i] = y[i - 1]
        b[i] = (y[i] - y[i-1])/h[i] - (2*c[i] + c[i+1])*h[i]/3
        d[i] = (c[i+1] - c[i])/(3*h[i])
    
    result = []
    for x0 in interpDots:
        i = 0
        for k in range(1, n):
            if x[k-1] <= x0 <= x[k]:
                i = k
                break
        result.append(a[i] + b[i]*(x0 - x[i-1]) + c[i]*(x0 - x[i-1])**2 + d[i]*(x0 - x[i-1])**3)

    return result

def toPlot(x, y):
    """
    Построить график интерполируемой функции.

    Строит график в отдельном окне, на котором красными точками отмечены 
    значения функции встроенными средствами matplotlib, а зеленым - 
    кривая, которая построена из значений списка, полученного функцией Splines.
    """
    x_new = np.linspace(x[0], x[-1], (x[-1] - x[0])*10)
    
    ax = plt.gca()
    ax.grid()
    ax.scatter(x, y, c='red')
    ax.plot(x_new, Spline(x_new, x, y), c='green')
    plt.show()

if __name__ == '__main__':
    x = np.linspace(-5, 5, 11, dtype=int)
    y = np.sin(np.pi * x)
    toPlot(x, y)