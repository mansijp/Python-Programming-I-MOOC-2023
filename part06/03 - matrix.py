def generate_matrix():
    matrix = []
    with open("src/matrix.txt") as mat:
        for line in mat:
            line = line.replace("\n", "")
            row = [int(i) for i in (line.split(","))]
            matrix.append(row)
        return(matrix)

def matrix_max():
    matrix = generate_matrix()
    n = max(matrix[0])
    for i in range(len(matrix)):
        if max(matrix[i]) > n:
            n = max(matrix[i])
    return(n)

def row_sums():
    matrix = generate_matrix()
    sums = []
    for i in range(len(matrix)):
        sums.append(sum(matrix[i]))
    return (sums)

def matrix_sum():
    matrix_sums = row_sums()
    return (sum(matrix_sums))

def main():
    print(matrix_max())
    print(row_sums())
    print(matrix_sum())


