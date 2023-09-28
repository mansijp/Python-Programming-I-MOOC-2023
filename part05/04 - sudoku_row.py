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

if __name__ == "__main__":
    print(row_correct([
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]], 0))
