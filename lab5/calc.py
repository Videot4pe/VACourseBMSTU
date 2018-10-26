from math import log, exp
from config import Es

StatSumm = [[1.0, 4.05, 5.15],
            [1.0, 4.30, 5.98],
            [1.0025, 4.44, 6.4],
            [1.020, 4.57, 6.96],
            [1.0895, 4.65, 7.41]]
StatSumm4 = 11.0
StatSumm5 = 15.0

def Q_i(t, i):
    index = (int)((t-4000)/4000 + 0.5)

    if i == 4:
        return StatSumm4
    elif i == 5:
        return StatSumm5
    else:
        return StatSumm[index][i-1]

def Z_i(i):
    return i-1

def E_i(i):
    return Es[i-1]

def delta_E_i(g, t, i):
    return (8.61 * 1e-5 * t *
            log((1 + Z_i(i+1) * Z_i(i+1) * g/2) *
                (1 + g/2) / (1 + Z_i(i) * Z_i(i) * g/2)))

def k_i_zv(t, g, i):
    dE = delta_E_i(g, t, i)
    _exp = exp(-(E_i(i)-dE) * 11603 / t)
    
    return 2*2.415e-3 * pow(t, 1.5) * _exp * Q_i(t, i+1) / Q_i(t, i)

def alpha(g, t):
    return 0.285 * 1e-11 * g * t * g * t * g * t

def _gamma(g, ve, x_i, t):
    sum = 0
    for i in range(2, 6):
        sum += (exp(x_i[i-1]) * Z_i(i) * Z_i(i)) / (1 + Z_i(i) * Z_i(i) * g/2)
    return (5.87 * 1e10 * (exp(ve)/(1+g/2) + sum) / (t * t * t)) - g * g
