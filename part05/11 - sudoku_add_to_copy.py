def print_sudoku(sudoku: list):
    for i in range(len(sudoku[0])):
        if (i)%3 == 0 and i!=0:
            print()
        tempString = ""
        for j in range(len(sudoku[i])):
            if (j)%3 == 0 and j!=0:
                tempString += " "
            if sudoku[i][j] == 0:
                tempString += "_ "
            else:
                tempString += str(sudoku[i][j]) + " "
        print(tempString)

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    copyGrid = [r.copy() for r in sudoku]
    copyGrid[row_no][column_no] = number 
    return (copyGrid)

def main():
    sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 5, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    grid_copy = copy_and_add(sudoku, 1, 1, 5)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)