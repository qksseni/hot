import random

a = 2
b = 2
A = [[ random.randint(1,10) for i in range (a) ] for j in range (b)]
print(A)

def det2 (n):
    return (n[0][0]*n[1][1] - n[0][1]*n[1][0])
    
print ( det2 (A) )

a = 3
b = 3
A = [[ random.randint(1,10) for i in range (a) ] for j in range (b)]
print(A)

def det3 (n):
    return (n[0][0] * n[1][1] * n[2][2]
        + n[0][1] * n[1][2] * n[2][0]
        + n[0][2] * n[1][0] * n[2][1]
        - n[0][2] * n[1][1] * n[2][0]
        - n[0][0] * n[1][2] * n[2][1]
        - n [0][1] * n[1][0] * n[2][2])
    
print ( det3 (A) )
