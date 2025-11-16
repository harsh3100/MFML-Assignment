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


aug_matrix = [
    [2, 1, -1,  8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]

result = gaussian_elimination(aug_matrix)

print("Row Echelon Form:")
for row in result:
    print(row)
