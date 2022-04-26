T0 = 293
T1 = 400
Xc = 50
T = [T0 for _ in range(0,Xc+1)]
xl = 0
xr = 1
dx = (xr - xl)/Xc
alpha = 111e-6
dt = 0.5 * ((dx ** 2) / alpha)
L = 1e-2
x = [[293 for _ in range(0,Xc+1)]]
t = [ 0 for _ in range(xl, Xc + 1)]
b = 0
while b <= 99:
    x.append(t)
    b = b+1
for n in range (0, 100):
    x[n][0] = 293
    x[n][Xc] = 400
for n in range (0,100):
    for i in range (1,Xc):
        x[n+1][i] = x[n][i] + ((alpha * dt)/(dx ** 2)) * (x[n][i+1] - 2 * x[n][i] + x[n][i-1])
X = [round (xa,2) for xa in x[-1]]
print (X)
