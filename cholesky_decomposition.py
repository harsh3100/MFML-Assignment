import math

def cholesky_manual(A):
    l11 = math.sqrt(A[0][0])
    l21 = A[1][0] / l11
    l31 = A[2][0] / l11

    l22 = math.sqrt(A[1][1] - (l21 * l21))
    l32 = (A[2][1] - (l31 * l21)) / l22

    l33 = math.sqrt(A[2][2] - (l31*l31 + l32*l32))

    L = [
        [l11, 0,   0],
        [l21, l22, 0],
        [l31, l32, l33]
    ]

    return L


A = [
    [25, 15, -5],
    [15, 18,  0],
    [-5,  0, 11]
]

L = cholesky_manual(A)
for row in L:
    print(row)
