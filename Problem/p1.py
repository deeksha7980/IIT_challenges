def sums(matrix):
    n = len(matrix)
    sumss = 0
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1:
                sumss += matrix[i][j]
            elif j == 0 or j == n - 1: 
                sumss += matrix[i][j]
            elif i == j:
                sumss += matrix[i][j]
            elif i + j == n - 1:
                sumss += matrix[i][j]
    print(sumss)


matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 1],
    [2, 3, 4, 5, 6],
    [7, 8, 9, 1, 2],
    [3, 4, 5, 6, 7]
]
sums(matrix)
