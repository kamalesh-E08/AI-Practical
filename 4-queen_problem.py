def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
    return True

def solve_n_queens(board, col):
    if col>= len(board): 
        return True

    for i in range(len(board)): 
        if is_safe(board, i, col):
            board[i][col]=1 
            if solve_n_queens(board, col + 1): 
                return True
            board[i][col] = 0   
    return False

def print_solution(board):
    for row in board: 
        print(''.join(['Q' if x == 1 else'.' for x in row])) 
        print()

def solve_4_queens():
    board = [[0 for _ in range(4)] for _ in range(4)]
    if solve_n_queens(board, 0):
        print("Solution exists:")
        print_solution(board)
    else:
        print("No solution exists.")

if  __name__ =="__main__":
    solve_4_queens()