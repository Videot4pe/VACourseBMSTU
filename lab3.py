from  math import cos, pi, sin
import numpy as np

def get_table(a, b, n):
    step = abs(a - b) / n
    xs = []
    ys = []
    for x in np.arange(a, b, step):
        xs.append(x)
        ys.append(x**3)
    
    return xs, ys


def nearest(lst, x):
    a = 0
    b = len(lst) - 1
    while a < b:
        m = int((a + b) / 2)
        if x > lst[m]:
            a = m + 1
        else:
            b = m
    return b

def print_table(x, y):
    print('\n\nx          y')
    for i in range(len(x)):
        print('{:.1f}      {:.1f}'.format(x[i], y[i]))
    print('\n')

def spline_interpolation(xs, ys, n, x):
    pos = nearest(xs, x)
    h = [0]*(n)
    A = [0]*(n)
    B = [0]*(n)
    D = [0]*(n)
    F = [0]*(n)
    a = [0]*(n)
    b = [0]*(n)
    c = [0]*(n+1)
    d = [0]*(n)
    k = [0]*(n+1)
    e = [0]*(n+1)
    
    
    for i in range(1, n):
        h[i] = xs[i] - xs[i - 1]
    
    for i in range(2, n):
        A[i] = h[i-1]
        B[i] = -2 * (h[i - 1] + h[i])
        D[i] = h[i]
        F[i] = -3 * ((ys[i] - ys[i - 1]) / h[i] - (ys[i - 1] - ys[i - 2]) / h[i - 1])
    
    for i in range(2, n):
        k[i + 1] = D[i] / (B[i] - A[i] * k[i])
        e[i + 1] = (A[i] * e[i] + F[i]) / (B[i] - A[i] * k[i])
    
    for i in range(n - 2, -1, -1):
        c[i] = k[i + 1] * c[i + 1] + e[i + 1]

    for i in range(1, n):
        a[i] = ys[i - 1]
        b[i] = (ys[i] - ys[i - 1]) / h[i] - h[i] / 3 * (c[i + 1] + 2 * c[i])
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])
    
    return a[pos] + b[pos] * (x - xs[pos - 1]) + c[pos] * ((x - xs[pos - 1]) ** 2) + d[pos] * ((x - xs[pos - 1]) ** 3)

a = float(input('Input left border: '))
b = float(input('Input right border: '))
n = int(input('Input n: '))

xss, yss = get_table(a, b, n)

print_table(xss, yss)

x = float(input('Input x: '))

result = spline_interpolation(xss, yss, n, x)
real_result = x**3

print("Result:  ", result)
print("Real result:  ", real_result)
