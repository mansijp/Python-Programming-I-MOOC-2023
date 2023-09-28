def column_correct(sudoku: list, column_no: int):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    column = []
    for i in range(1, 10):
        column.append(sudoku[i-1][column_no])
    print(column)
    for i in range(1, 10):
        if i in column:
            if i in numbers:
                numbers.remove(i)
    if len(numbers) == column.count(0):
        return (True)
    else:
        return (False)
    
if __name__ == "__main__":
    print(column_correct([
  [ 9, 0, 1, 0, 8, 0, 3, 0, 1 ],
  [ 2, 2, 0, 0, 5, 0, 7, 0, 0 ],
  [ 0, 2, 0, 3, 0, 0, 4, 0, 4 ],
  [ 2, 9, 4, 0, 0, 0, 2, 0, 0 ],
  [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
  [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
  [ 0, 0, 7, 8, 0, 3, 9, 8, 6 ],
  [ 3, 0, 1, 0, 0, 0, 0, 0, 1 ],
  [ 3, 0, 0, 0, 2, 0, 2, 0, 1 ]], 1))
    