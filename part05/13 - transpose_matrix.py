def transpose(matrix: list):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

if __name__ == "__main__":
    matrix = [[1,2],[1,2]]
    transpose(matrix)
    print(matrix)
    

    