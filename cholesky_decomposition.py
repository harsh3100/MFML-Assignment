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

print("Enter the 3x3 matrix (row by row):")
A = []
for i in range(3):
    row = list(map(float, input(f"Row {i+1} (space-separated): ").split()))
    A.append(row)

print("\nInput Matrix:")
for row in A:
    print(row)

L = cholesky_manual(A)
print("\nCholesky Decomposition (Lower Triangular Matrix L):")
for row in L:
    print(row)

"""
OUTPUT

Enter the 3x3 matrix (row by row):
Row 1 (space-separated): 25 15 -5
Row 2 (space-separated): 15 18 0
Row 3 (space-separated): -5 0 11

Input Matrix:
[25.0, 15.0, -5.0]
[15.0, 18.0, 0.0]
[-5.0, 0.0, 11.0]

Cholesky Decomposition (Lower Triangular Matrix L):
[5.0, 0, 0]
[3.0, 3.0, 0]
[-1.0, 1.0, 3.0]

"""
