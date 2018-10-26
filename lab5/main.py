from slau import get_start_values, solve
from math import exp

def main():
    p, t = map(float, input('Press and temp: ').split())
    ve, x_i = get_start_values(p, 1000)
    res = [0.0]*6
    g = 0.0
    res[0] = ve
    for i in range(1, 6):
        res[i] = x_i[i-1]

    for temp in range(1000, int(t)+1, 1000):
        res, g = solve(ve, x_i, p, t, g)
        #print(res)
        ve = res[0]
        for i in range(5):
            x_i[i] = res[i+1]

    print('ne* = %.3f' %exp(res[0]))
    if (res):
        for i in range(1, 6):
            print('n%d* = %.3f' %(i ,exp(res[i])))
        print('gamma = %.3f' %g)
    else:
        print('slau not solve')

main()

