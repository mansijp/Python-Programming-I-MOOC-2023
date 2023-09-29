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

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number

def main():
    sudoku  = [[ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
               [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
               [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
               [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
               [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
               [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
               [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
               [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
               [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ]]
    print_sudoku(sudoku)
    add_number(sudoku, 0, 1, 2)
    add_number(sudoku, 1, 2, 7)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)