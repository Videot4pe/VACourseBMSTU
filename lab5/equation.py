from calc import alpha, Z_i
from math import exp

def equation_14(ve, x_i, x_il, lnKi_zv):
    return ve + x_il - x_i - lnKi_zv

def equation_5(p, t, ve, x_i, g):
    sum = 0
    pkt = -7242.0 * p / t
    a = alpha(g, t)

    for i in range(5):
        sum += exp(x_i[i])

    return pkt + exp(ve) + sum - a

def equation_6(ve, x_i):
    sum = 0
    for i in range(1, 5):
        sum += Z_i(i+1) * exp(x_i[i])

    return exp(ve)-sum
