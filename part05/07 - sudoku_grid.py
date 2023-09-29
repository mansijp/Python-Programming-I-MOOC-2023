# Checking row
def row_correct(sudoku: list, row_no: int):
    numbers = [1,2,3,4,5,6,7,8,9]
    for i in range(1, 10):
        if i in sudoku[row_no]:
            if i in numbers:
                numbers.remove(i)
    if len(numbers) == sudoku[row_no].count(0):
        return (True)
    else:
        return (False)

# Checking column
def column_correct(sudoku: list, column_no: int):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    column = []
    for i in range(1, 10):
        column.append(sudoku[i-1][column_no])
    for i in range(1, 10):
        if i in column:
            if i in numbers:
                numbers.remove(i)
    if len(numbers) == column.count(0):
        return (True)
    else:
        return (False)

# Checking block
def block_correct(sudoku: list, r: int, c: int):
    n = []
    numbers = [1,2,3,4,5,6,7,8,9]
    for i in range(r, r+3):
        for j in range(c, c+3):
            n.append(sudoku[i][j])
    for i in range(1, 10):
        if (i in n) and (i in numbers):
            numbers.remove(i)
            n.remove(i)
    if (len(n) == len(numbers)) and (sum(n) == 0):
        return (True)
    else:
        return (False)

# Checking grid
def sudoku_grid_correct(sudoku: list):
    for m in range(0, 9):
        if not row_correct(sudoku, m):
            return (False)
        if not column_correct(sudoku, m):
            return (False)
    for m in range(0, 9, 3):
        for n in range(0, 9, 3):
            if not block_correct(sudoku, m, n):
                return (False)
    return (True)

if __name__ == "__main__":
    print(sudoku_grid_correct([
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]]))