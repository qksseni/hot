import matplotlib.pyplot as plt

T0 = 293
T1 = 400
Xc = 50
rtol = 1e-4
xl = 0
xr = 1
L = 0.02
dx = (xr - xl)/Xc
alpha = 111e-6
dt = 0.5 * ((dx ** 2) / alpha)
LX = L / (Xc - 1)
L = [LX*i for i in range (Xc)]
x = [293 for _ in range (0, Xc)]
R = [999]
while max (R) >= rtol:
    R = []
    x.append ([T0] * Xc)
    N = len (x)-1
    x[N][0] = 293
    x[N][Xc - 1] = 400
    for i in range (1, Xc - 1):
        x[N][i] = x[N - 1][i] + ((alpha * dt) / (dx**2)) * (x[N - 1][i + 1] - 2*x[N - 1][i] + x[N - 1][i - 1])
    for i in range ( 0 , Xc ):
        r = abs ( x[N][i] - x[N-1][i] )
        R.append (r)
L = [ round (xa , 4) for xa in L]
X = [ round (xa , 2) for xa in x [-1] ]
print ( "Распределение температур =" , X )
print ( "Координата X узла =" , L )
print ( "Количество итераций = " , len (x) )
plt.plot (L , X)
plt.xlabel ( "Координата X узла , м")
plt.ylabel ( "Температура , К")
plt.grid (True)
plt.title ( "Распределение температуры по стержню")
plt.show()
