def gaussian_elimination(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        if matrix[i][i] == 0:
            for k in range(i + 1, rows):
                if matrix[k][i] != 0:
                    matrix[i], matrix[k] = matrix[k], matrix[i]   # swap
                    break
        if matrix[i][i] == 0:
            continue
        pivot = matrix[i][i]
        for j in range(i, cols):
            matrix[i][j] = matrix[i][j] / pivot
        for k in range(i + 1, rows):
            factor = matrix[k][i]
            for j in range(i, cols):
                matrix[k][j] -= factor * matrix[i][j]
    return matrix

print("Enter the number of equations:")
n = int(input())

print(f"\nEnter the augmented matrix ({n}x{n+1}) row by row:")
aug_matrix = []
for i in range(n):
    row = list(map(float, input(f"Row {i+1} (space-separated): ").split()))
    aug_matrix.append(row)

print("\nInput Augmented Matrix:")
for row in aug_matrix:
    print(row)

result = gaussian_elimination(aug_matrix)
print("\nRow Echelon Form:")
for row in result:
    print(row)

"""
OUTPUT


Example execution:
Enter the number of equations:
3

Enter the augmented matrix (3x4) row by row:
Row 1 (space-separated): 2 1 -1 8
Row 2 (space-separated): -3 -1 2 -11
Row 3 (space-separated): -2 1 2 -3

Input Augmented Matrix:
[2.0, 1.0, -1.0, 8.0]
[-3.0, -1.0, 2.0, -11.0]
[-2.0, 1.0, 2.0, -3.0]

Row Echelon Form:
[1.0, 0.5, -0.5, 4.0]
[0.0, 1.0, -1.0, -2.0]
[0.0, 0.0, 1.0, 1.0]
"""

