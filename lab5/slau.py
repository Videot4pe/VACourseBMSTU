from calc import k_i_zv, _gamma, Z_i
from math import sqrt, log, exp
from config import EPS
from equation import equation_14, equation_5, equation_6

def solve_square(a, b, c):
    D = b*b - 4*a*c
    if D < 0:
        D = abs(D)

    return (-b + sqrt(D)) / 2 / a

def get_start_values(p, t):
    x_i = [0.0]*5
    K = k_i_zv(t, 0, 1)*1e18
    pkt = p*7242.0 / t

    ne = solve_square(1, 2*K, -pkt*K) * 1e-18

    ve = log(ne)
    x_i[1] = ve
    x_i[0] = log(pkt - 2*ne)
    x_i[2] = -100
    x_i[3] = -120
    x_i[4] = -140

    return ve, x_i

def solve(ve, x_i, p, t, g):
    delta = [0.0]*6
    result = [0.0]*6
    matrix = []
    for i in range(6):
        line = []
        for i in range(7):
            line.append(0)
        matrix.append(line)

    result[0] = ve
    for i in range(1, 6):
        result[i] = x_i[i-1]

    while(True):
        matrix = calc_A(matrix, result[0], result[1:], g, t, p)
        copy_a = copy_matrix(matrix)
        delta = gauss(copy_a, delta)

        for i in range(6):
            result[i] += delta[i]
        g = calc_gamma(0, 4, result[0], result[1:], t)
        if condition(delta, result):
            break

    #print(result)
    return result, g

def condition(delta, x):
    m = abs(delta[0]/x[0])

    for i in range(1, 6):
        n = abs(delta[i]/x[i])
        if n > m:
            m = n

    if m < EPS:
        return 1
    else:
        return 0

def calc_gamma(a, b, ve, x_i, t):
    c = 0.0

    while (b-a > EPS):
        c = (a+b)/2
        if _gamma(b, ve, x_i, t) * _gamma(c, ve, x_i, t) < 0:
            a = c
        else:
            b = c
    
    return c

def gauss(mat, result):
    for i in range(6):
        max = i

        for j in range(i, 6):
            if mat[j][i]:
                max = j
                break

        if (max == 6):
            break
        
        mat[i], mat[max] = mat[max], mat[i]

        for j in range(i+1, 6):
            for k in range(i+1, 7):
                #print(mat[i][k], mat[j][i], mat[i][i])
                mat[j][k] -= mat[i][k] * (mat[j][i] / mat[i][i])
            mat[j][i] = 0

    for i in range(6-1, -1, -1):
        result[i] = mat[i][6]
        for j in range(i+1, 6):
            result[i] -= mat[i][j] * result[j]
        result[i] /= mat[i][i]

    return result

def copy_matrix(matrix):
    copy = []
    for line in matrix:
        copy_line = []
        for el in line:
            copy_line.append(el)
        copy.append(line)

    return copy

def calc_A(A, ve, x_i, g, t, p):
    for i in range(6):
        for j in range(7):
            A[i][j] = 0
            
    for i in range(4):
        A[i][0] = 1
        A[i][i+1] = -1
        A[i][i+2] = 1
        A[i][6] = -equation_14(ve, x_i[i], x_i[i+1], log(k_i_zv(t, g, i+1)))


    A[4][0] = exp(ve)
    for i in range(1, 6):
        A[4][i] = exp(x_i[i-1])
    A[4][6] = -equation_5(p, t, ve, x_i, g)

    A[5][0] = exp(ve)
    for i in range(2, 6):
        A[5][i] = -Z_i(i) * exp(x_i[i-1])
    A[5][6] = -equation_6(ve, x_i)
    
    return A
