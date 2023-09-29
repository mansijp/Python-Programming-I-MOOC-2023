def play_turn(game_board: list, x: int, y: int, piece: str):
    if (y>2 or y<0) or (x>2 or x<0):
        return(False)
    if game_board[y][x] == "":
        game_board[y][x] = piece
        return(True)
    else:
        return(False)
    
def main():
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)
