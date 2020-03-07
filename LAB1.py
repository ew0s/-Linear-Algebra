inp = open("input.txt", "r")
def scan_list():
    str = inp.readline().split()
    n, m = int(str[0]), int(str[1])
    A = [[0] * m for i in range(n)]
    B = list(map(float, inp.readline().split()))
    k = 0
    for i in range(n):
        for j in range(m):
            A[i][j] = B[k]
            k = k + 1
    return A

def num_mult_matrix(t, Ar = []):
    for i in range(len(Ar)):
        for j in range(len(Ar[i])):
            Ar[i][j] = Ar[i][j] * t
    return Ar

def plus_matrix(myA = [], myB = []):
    for i in range(len(myA)):
        for j in range(len(myA[i])):
            myA[i][j] += myB[i][j]
    return myA

def tr_matrix(myC = []):
    T = [[0] * len(myC) for i in range(len(myC[0]))]
    for i in range(len(myC)):
        for j in range(len(myC[i])):
            T[j][i] = myC[i][j]
    return T

def mult_matrix(Am = [], Bm = []):
    P = [[0] * len(Bm[0]) for i in range(len(Am))]
    for i in range(len(Am)):
        for j in range(len(Bm[0])):
            for k in range(len(Am[0])):
                P[i][j] += Am[i][k] * Bm[k][j]
    return P


str = inp.readline().split()
a, b = float(str[0]), float(str[1])
A = scan_list()
B = scan_list()
C = scan_list()
D = scan_list()
F = scan_list()

X1 = num_mult_matrix(a, A)
X2 = tr_matrix(B)
X2 = num_mult_matrix(b, X2)
f = 0

if len(X1) != len(X2) or len(X1[0]) != len(X2[0]):
    f = 1
else:
    X1 = plus_matrix(X1, X2)

X1 = tr_matrix(X1)

if f == 0 and (len(C[0]) == len(X1)):
    X3 = mult_matrix(C, X1)
else:
    f = 1

if f == 0 and (len(X3[0]) == len(D)):
    X4 = mult_matrix(X3, D)
else:
    f = 1

F = num_mult_matrix(-1, F)

if f == 1 or len(X4) != len(F) or len(X4[0]) != len(F[0]):
    f = 1
else:
    X4 = plus_matrix(X4, F)

if f == 1:
    with open('output.txt', 'w') as f:
        print(0, file = f)
else:
    with open('output.txt', 'w') as f:
        print(1, file=f)
        print(len(X4), len(X4[0]), file=f)
        for i in range(len(X4)):
            for j in range(len(X4[0])):
                print(X4[i][j], end=' ', file=f)
            print(file=f)
