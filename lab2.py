import numpy as np
from math import ceil

def func(x, y):
    return x*x + y*y

def nearest_number(lst, x):
    a = 0
    b = len(lst) - 1
    while a < b:
        m = int((a + b) / 2)
        if x > lst[m]:
            a = m + 1
        else:
            b = m
    return b

def recurs_function(xs, ys):
    l = len(xs)
    if l == 1:
        return ys[0]
    else:
        return (recurs_function(xs[:-1], ys[:-1]) - recurs_function(xs[1:], ys[1:])) / (xs[0] - xs[l - 1])


def newton_interpolation(lst_x, lst_z, x):
    i = nearest_number(lst_x, x)
    z_x = lst_z[0]
    for i in range(1, len(lst_x)):
        k = 1
        for j in range(i):
            k *= (x - lst_x[j])
        dd = recurs_function(lst_x[:i+1], lst_z[:i+1])
        z_x += (k * dd)
    return z_x


def start_interpolation():
    xs, ys, zs = create_table()
    print_table(xs, ys, zs)
    x = float(input('input x: '))
    y = float(input('input y: '))
    while (x < 0) or (x > 5) or (y < 0) or (y > 5):
        print("Wrong borders")
        x = float(input('input x: '))
        y = float(input('input y: '))
    
    n = int(input('input xn: '))
    m = int(input('input yn: '))

    i_x = nearest_number(xs, x)
    i_y = nearest_number(ys, y)
    lx = len(xs)
    ly = len(ys)
    
    if i_y - (m + 1) / 2 < 0:
        sample_y = ys[:int(i_y + int(ceil((m + 1) / 2)) + 1)]
        sample_z = zs[:int(i_y + int(ceil((m + 1) / 2)) + 1)]
    elif ly < i_y + (m + 1) / 2:
        sample_y = ys[i_y - int(ceil((m + 1) / 2)):]
        sample_z = zs[i_y - int(ceil((m + 1) / 2)):]
    else:
        if m % 2 != 0:
            sample_y = ys[i_y - int(ceil((m + 1) / 2)): i_y + int(ceil((m + 1) / 2))]
            sample_z = zs[i_y - int(ceil((m + 1) / 2)): i_y + int(ceil((m + 1) / 2))]
        else:
            sample_y = ys[i_y - int(ceil((m + 1) / 2)) - 1: i_y + int(ceil((m + 1) / 2))]
            sample_z = zs[i_y - int(ceil((m + 1) / 2)) - 1: i_y + int(ceil((m + 1) / 2))]

    left = 0
    right = 0
    
    if i_x - (n + 1) / 2 < 0:
        sample_x = xs[:int(i_x + int(ceil((n + 1) / 2)) + 1)]
        right = i_x + int(ceil((n + 1) / 2) + 1)
    elif lx < i_x + (n + 1) / 2:
        sample_x = xs[i_x - int(ceil((n + 1) / 2)):]
        left = i_x - int(ceil((n + 1) / 2))
        right = 6
    elif n % 2 != 0:
        sample_x = xs[i_x - int(ceil((n + 1) / 2)): i_x + int(ceil((n + 1) / 2))]
        left = i_x - int(ceil((n + 1) / 2))
        right = i_x + int(ceil((n + 1) / 2))
    else:
        sample_x = xs[i_x - int(ceil((n + 1) / 2)) - 1: i_x + int(ceil((n + 1) / 2))]
        left = i_x - int(ceil((n + 1) / 2)) - 1
        right = i_x + int(ceil((n + 1) / 2))

    for i in range(len(sample_z)):
        sample_z[i] = sample_z[i][int(left):int(right)]

    answ = []

    for i in range(len(sample_y)):
        answ.append(newton_interpolation(sample_x, sample_z[i], x))

    result = func(x, y)
    print('Real result: {}'.format(result))
    return newton_interpolation(sample_y, answ, y)

def create_table():
    x = []
    y = []
    z = []

    for i in range (6):
        y.append(i)
        x.append(i)
    for current_x in np.arange(0, 6, 1):
        line = []
        for current_y in np.arange(0, 6, 1):
            line.append(func(current_x, current_y))
        z.append(line)
    return x, y, z
   
def print_table(x, y, z):
    print ('\n')
    s = "    0   1   2   3   4   5"
    print(s)
    k = 0
    s1 = str(k) + "|  " + str(z[k][0]) + "   " + str(z[k][1]) + "   " + str(z[k][2]) + "   " + str(z[k][3]) + "   " + str(z[k][4]) + "  " + str(z[k][5])
    print(s1)
    k = k + 1
    s1 = str(k) + "|  " + str(z[k][0]) + "   " + str(z[k][1]) + "   " + str(z[k][2]) + "   " + str(z[k][3]) + "  " + str(z[k][4]) + "  " + str(z[k][5])
    print(s1)
    k = k + 1
    s1 = str(k) + "|  " + str(z[k][0]) + "   " + str(z[k][1]) + "   " + str(z[k][2]) + "   " + str(z[k][3]) + "  " + str(z[k][4]) + "  " + str(z[k][5])
    print(s1)
    k = k + 1
    s1 = str(k) + "|  " + str(z[k][0]) + "   " + str(z[k][1]) + "  " + str(z[k][2]) + "  " + str(z[k][3]) + "  " + str(z[k][4]) + "  " + str(z[k][5])
    print(s1)
    k = k + 1
    s1 = str(k) + "|  " + str(z[k][0]) + "  " + str(z[k][1]) + "  " + str(z[k][2]) + "  " + str(z[k][3]) + "  " + str(z[k][4]) + "  " + str(z[k][5])
    print(s1)
    k = k + 1
    s1 = str(k) + "|  " + str(z[k][0]) + "  " + str(z[k][1]) + "  " + str(z[k][2]) + "  " + str(z[k][3]) + "  " + str(z[k][4]) + "  " + str(z[k][5])
    print(s1)
    print('\n')

print('Function z = x^2 + y^2')
my_result = start_interpolation()

print('Result: {}'.format(my_result))
