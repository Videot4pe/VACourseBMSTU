import numpy
import matplotlib.pyplot as plt

def f(k, x):
    res = 0
    for i in range(len(k)):
        res += k[i]* x ** i
    return res
    

def fi_curried(k):
    def fi(x):
        return x ** k
    return fi

def y_curried(x_arr, y_arr):
    def y(x):
        return y_arr[x_arr.index(x)]
    return y

def Dot_product(x_arr, ro_arr, f, psi):
    res = 0
    for i in range(len(x_arr)):
        res += ro_arr[i]*f(x_arr[i])*psi(x_arr[i])
    return res
        
def SLAY(x_arr, y_arr, ro_arr, n):
    v1 = []
    M1 = []
    y = y_curried(x_arr, y_arr)
    for k in range(0, n+1):
        fi_k = fi_curried(k)
        arr = []
        for m in range(0, n+1):
            fi_m = fi_curried(m)
            arr.append(Dot_product(x_arr, ro_arr, fi_k, fi_m))
        v1.append(Dot_product(x_arr, ro_arr, fi_k, y))
        M1.append(arr)
    return numpy.linalg.solve(M1, v1)

n = int(input('Power: '))

file = open('data.txt', 'r')
x_arr = []
y_arr = []
ro_arr = []

for i in file.read().split('\n'):
    arr = i.split()
    x_arr.append(float(arr[0]))
    y_arr.append(float(arr[1]))
    ro_arr.append(float(arr[2]))
file.close()



coef = SLAY(x_arr, y_arr, ro_arr, n)


x_arr_new = numpy.linspace(x_arr[0], x_arr[len(x_arr)-1], 10)
y_arr_new = [f(coef, x) for x in x_arr_new]
plt.figure("Approximation")
plt.plot(x_arr_new, y_arr_new, label = 'Approximation')

plt.scatter(x_arr, y_arr, color='b', s=10, alpha=.5, label="Real result")

plt.grid(True)
plt.xlabel(u'X')
plt.ylabel(u'Y')
plt.legend()

plt.show()
