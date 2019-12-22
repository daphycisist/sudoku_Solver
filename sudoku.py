#Sample Sudoku Board
# 7 8 0    4 0 0    1 2 0
# 6 0 0    0 7 5    0 0 9
# 0 0 0    6 0 1    0 7 8
                         
# 0 0 7    0 4 0    2 6 0
# 0 0 1    0 5 0    9 3 0
# 9 0 4    0 6 0    0 0 5
                         
# 0 7 0    3 0 0    0 1 2
# 1 2 0    0 0 7    4 0 0
# 0 4 9    2 0 6    0 0 7

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def boardPrinter(board):
    for i in range(0,9):
        if i % 3 == 0 and i != 0:
            print("                         ")
        for j in range(0,9):
            if j % 3 == 0 and j != 0:
                print("   ", end="")
            
            if j == 8:
                print(board[i][j]) #create new line only at pos 8
            else:
                print(str(board[i][j]) + " ", end="")


def emptyfield(board):
    #loops through fields (x,y)
    for i in range(0,9):
        for j in range(0,9):
            if board[i][j] == 0:
                return (i,j) #return position of empty field
    return None # If None empty fields return none

#takes in the board, the number to validate and the position of the empty field
def validNumber(board, num, pos):
    #to check valid number 3 conditons are met
    # 1) Check if number does not exist in row
    for i in range(0,9):
        if board[i][pos[1]] == num and i != pos[0]:
            # print("Found in Row")
            return False

    # # 2) Check if number does not exist in column
    for i in range(0,9):
        if board[pos[0]][i] == num and i != pos[1]:
            # print("Found in Col")
            return False

    # 3) Check if Number does not exist in smaller box
    # Check Which Box the emptyfield falls under.
    boxXAxis = (pos[1] // 3 ) * 3 # starting x pos for box, + 3 for end pos
    boxYAxis = (pos[0] // 3 ) * 3

    #loop through all values in small box
    count = 0
    for i in range(boxYAxis, boxYAxis + 3):
        for j in range(boxXAxis, boxXAxis + 3):
            if board[i][j] == num and (i,j) != pos:
                # print("Found in Box")
                return False
            # to view my smaller box
            # count += 1
            # if count % 3 == 0:
            #     print(board[i][j])
            # else:
            #     print(board[i][j], end="")
    return True #if none of the conditions are met, then value is valid


def boardSolve(board):
    #check if no empty space
    blank = emptyfield(board)
    if not blank:
        return True
    else:
        row, col = blank
        
    #only values 1-9 are permitted in sudoku
    for i in range(1,10):
        if validNumber(board, i, (row, col)):
            board[row][col] = i
            #if number is valid, run func to check if board is solved
            if boardSolve(board):
                return True
            
            #backtracking to set previous value to position to blank
            board[row][col] = 0

    return False



boardPrinter(board)
print("-----------------")
boardSolve(board)
boardPrinter(board)