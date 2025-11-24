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

print("Enter the dimensions of the matrix:")
m = int(input("Number of rows: "))
n = int(input("Number of columns: "))

print(f"\nEnter the {m}x{n} matrix (row by row):")
A = []
for i in range(m):
    row = list(map(float, input(f"Row {i+1} (space-separated): ").split()))
    A.append(row)

print("\nInput Matrix:")
for row in A:
    print(row)

Q = gram_schmidt(A)
print("\nOrthonormal Matrix Q (Gram-Schmidt):")
for row in Q:
    print(row)

"""
OUTPUT

Enter the dimensions of the matrix:
Number of rows: 3
Number of columns: 3

Enter the 3x3 matrix (row by row):
Row 1 (space-separated): 1 1 1
Row 2 (space-separated): 1 2 3
Row 3 (space-separated): 1 3 6

Input Matrix:
[1.0, 1.0, 1.0]
[1.0, 2.0, 3.0]
[1.0, 3.0, 6.0]

Orthonormal Matrix Q (Gram-Schmidt):
[0.5773502691896258, -0.7071067811865478, 0.4082482904638614]
[0.5773502691896258, -3.14018491736755e-16, -0.8164965809277266]
[0.5773502691896258, 0.7071067811865471, 0.4082482904638636]

"""
