import math

def dot(x, y):
    return sum(x[i] * y[i] for i in range(len(x)))

def scalar_multiply(c, v):
    return [c * x for x in v]

def subtract(u, v):
    return [u[i] - v[i] for i in range(len(u))]

def norm(v):
    return math.sqrt(dot(v, v))

def gram_schmidt(A):
    m = len(A)
    n = len(A[0])
    Q = [[0.0] * n for _ in range(m)]
    U = []

    for j in range(n):
        v = [A[i][j] for i in range(m)]

        for k in range(j):
            qk = [Q[i][k] for i in range(m)]
            proj = scalar_multiply(dot(v, qk), qk)
            v = subtract(v, proj)

        u = v[:]
        U.append(u)

        length = norm(u)
        q = scalar_multiply(1/length, u)

        for i in range(m):
            Q[i][j] = q[i]

    return Q


A = [
    [1, 1, 1],
    [1, 2, 3],
    [1, 3, 6]
]

Q = gram_schmidt(A)
for row in Q:
    print(row)
