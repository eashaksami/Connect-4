# # Python3 program to find the next optimal move for a player
# player, opponent = 'x', 'o'
#
#
# # This function returns true if there are moves
# # remaining on the board. It returns false if
# # there are no moves left to play.
# def isMovesLeft(board):
#     for i in range(4):
#         for j in range(4):
#             if (board[i][j] == '_'):
#                 return True
#     return False
#
#
# # This is the evaluation function as discussed
# # in the previous article ( http://goo.gl/sJgv68 )
# def evaluate(b):
#     # Checking for Rows for X or O victory.
#     for row in range(4):
#         if (b[row][0] == b[row][1] and b[row][1] == b[row][2] and b[row][2] == b[row][3]):
#             if (b[row][0] == player):
#                 return 10
#             elif (b[row][0] == opponent):
#                 return -10
#
#     # Checking for Columns for X or O victory.
#     for col in range(4):
#
#         if (b[0][col] == b[1][col] and b[1][col] == b[2][col] and b[2][col] == b[3][col]):
#
#             if (b[0][col] == player):
#                 return 10
#             elif (b[0][col] == opponent):
#                 return -10
#
#     # Checking for Diagonals for X or O victory.
#     if (b[0][0] == b[1][1] and b[1][1] == b[2][2] and b[2][2] == b[3][3]):
#
#         if (b[0][0] == player):
#             return 10
#         elif (b[0][0] == opponent):
#             return -10
#
#     if (b[0][2] == b[1][2] and b[1][2] == b[2][1] and b[2][1] == b[3][0]):
#
#         if (b[0][2] == player):
#             return 10
#         elif (b[0][2] == opponent):
#             return -10
#
#     # Else if none of them have won then return 0
#     return 0
#
#
# # This is the minimax function. It considers all
# # the possible ways the game can go and returns
# # the value of the board
# def minimax(board, depth, isMax):
#     score = evaluate(board)
#
#     # If Maximizer has won the game return his/her
#     # evaluated score
#     if (score == 10 or depth == 2):
#         return score
#
#     # If Minimizer has won the game return his/her
#     # evaluated score
#     if (score == -10 or depth == 2):
#         return score
#
#     # If there are no more moves and no winner then
#     # it is a tie
#     if (isMovesLeft(board) == False):
#         return 0
#
#     # If this maximizer's move
#     if (isMax):
#         best = -1000
#
#         # Traverse all cells
#         for i in range(4):
#             for j in range(4):
#
#                 # Check if cell is empty
#                 if (board[i][j] == '_'):
#                     # Make the move
#                     board[i][j] = player
#                     print(board)
#                     print(depth)
#
#                     # Call minimax recursively and choose
#                     # the maximum value
#                     best = max(best, minimax(board,
#                                              depth + 1,
#                                              not isMax))
#
#                     # Undo the move
#                     board[i][j] = '_'
#         return best
#
#     # If this minimizer's move
#     else:
#         best = 1000
#
#         # Traverse all cells
#         for i in range(4):
#             for j in range(4):
#
#                 # Check if cell is empty
#                 if (board[i][j] == '_'):
#                     # Make the move
#                     board[i][j] = opponent
#                     print(board)
#                     print(depth)
#
#                     # Call minimax recursively and choose
#                     # the minimum value
#                     best = min(best, minimax(board, depth + 1, not isMax))
#
#                     # Undo the move
#                     board[i][j] = '_'
#         return best
#
#
# # This will return the best possible move for the player
# def findBestMove(board):
#     bestVal = -1000
#     bestMove = (-1, -1)
#
#     # Traverse all cells, evaluate minimax function for
#     # all empty cells. And return the cell with optimal
#     # value.
#     for i in range(4):
#         for j in range(4):
#
#             # Check if cell is empty
#             if (board[i][j] == '_'):
#
#                 # Make the move
#                 board[i][j] = player
#                 print("")
#                 print(board)
#
#                 # compute evaluation function for this
#                 # move.
#                 moveVal = minimax(board, 0, False)
#
#                 # Undo the move
#                 board[i][j] = '_'
#
#                 # If the value of the current move is
#                 # more than the best value, then update
#                 # best/
#                 if (moveVal > bestVal):
#                     bestMove = (i, j)
#                     bestVal = moveVal
#
#     print("The value of the best Move is :", bestVal)
#     print()
#     return bestMove
#
#
# # Driver code
# board = [
#     ['x', 'o', 'x', 'x'],
#     ['o', 'o', 'x', 'x'],
#     ['o', 'x', 'o', 'o'],
#     ['o', '_', '_', '_']
# ]
#
# bestMove = findBestMove(board)
#
# print("The Optimal Move is :")
# print("ROW:", bestMove[0], " COL:", bestMove[1])
#
# # This code is contributed by divyesh072019


'''def Minimax(gameState, isMaximizer, availableMoveRow): # availableMoveRow - row where we can give the next move
    remainingMoves = 7
    for i in range(7):
        if gameState[0][i] == '_':
            remainingMoves -= 1
    if(remainingMoves == 0):
        return
    if isMaximizer:
        for i in range(7):
            if gameState[0][i] == '_':
                gameState[5 - availableMoveRow[i]][i] = 'x'
                print(gameState)
                availableMoveRow[i]+=1
                Minimax(gameState, not isMaximizer, availableMoveRow)
                gameState[5 - availableMoveRow[i]][i] = '_'
                availableMoveRow[i]-=1
    else:
        for i in range(7):
            if gameState[0][i] == '_':
                gameState[5 - availableMoveRow[i]][i] = 'o'
                print(gameState)
                availableMoveRow[i]+=1
                Minimax(gameState, not isMaximizer, availableMoveRow)
                gameState[5 - availableMoveRow[i]][i] = '_'
                availableMoveRow[i]-=1 '''

'''def fun(n, i):

    if n == 0:
        return 1
    else:
        i += 1
        fun(n - 1, i)
        print(i)
i = 0
fun(5, i)'''



def WinningState(gameState):
    totalInARow = 0
    # x-axis check
    for i in range(6):
        totalInARow = 0
        for j in range(7 - 1):
            if gameState[5 - i][j] == 'x':
                if gameState[5 - i][j + 1] == 'x' and totalInARow < 4:  # array index out of bound
                    totalInARow += 1
                    if totalInARow == 3:
                        totalInARow += 1
                        return 1000
                else:
                    totalInARow = 0

            elif gameState[5 - i][j] == 'o':
                if gameState[5 - i][j + 1] == 'o' and totalInARow < 4:
                    totalInARow += 1
                    if totalInARow == 3:
                        totalInARow += 1
                        return -1000
                else:
                    totalInARow = 0
    totalInARow = 0

    # y-axis check
    for i in range(7):
        totalInARow = 0
        for j in range(6 - 1):
            if gameState[5 - j][i] == 'x':
                if gameState[5 - j - 1][i] == 'x' and totalInARow < 4:  # array index out of bound
                    totalInARow += 1
                    if totalInARow == 3:
                        totalInARow += 1
                        return 1000
                else:
                    totalInARow = 0

            elif gameState[5 - j][i] == 'o':
                if gameState[5 - j - 1][i] == 'o' and totalInARow < 4:
                    totalInARow += 1
                    if totalInARow == 3:
                        totalInARow += 1
                        return -1000
                else:
                    totalInARow = 0
    totalInARow = 0

    # Check positively sloped diaganols
    for c in range(7 - 3):
        for r in range(6 - 3):
            for k in range(3):
                if gameState[r + k][c + k] == 'x':
                    if gameState[r + k + 1][c + k + 1] == 'x':
                        totalInARow+= 1
                        if totalInARow == 3:
                            totalInARow+= 1
                            return 1000
                    else:
                        totalInARow = 0

            # totalInARow = 0

                elif gameState[r + k][c + k] == 'o':
                    if gameState[r + k + 1][c + k + 1] == 'o':
                        totalInARow+= 1
                        if totalInARow == 3:
                            totalInARow += 1
                            return -1000
                    else:
                        totalInARow = 0

            totalInARow = 0

    # Check negatively sloped diaganols
    for c in range(7 - 3):
        for r in range(3, 6):
            for k in range(4):
                if gameState[r - k][c + k] == 'x':
                    totalInARow+= 1
                else:
                    totalInARow = 0
                if totalInARow == 4:
                    return 1000
            totalInARow = 0
            for k in range(4):
                if gameState[r - k][c + k] == 'o':
                    totalInARow+= 1
                else:
                    totalInARow = 0
                if totalInARow == 4:
                    return -1000
            totalInARow = 0


    return 1

def getBoard():
    # board = [
    #     ['x', 'o', '_', '_', '_', 'x', 'x'],
    #     ['o', 'x', '_', 'o', 'x', 'o', 'x'],
    #     ['x', 'x', 'o', 'x', 'x', 'o', 'o'],
    #     ['o', 'o', 'o', 'x', 'x', 'x', 'o'],
    #     ['x', 'o', 'x', 'o', 'o', 'x', 'x'],
    #     ['x', 'o', 'x', 'x', 'o', 'x', 'x']
    # ]
    # board = [
    #     ['_', '_', '_', '_', '_', '_', '_'],
    #     ['_', '_', '_', '_', '_', '_', '_'],
    #     ['_', '_', '_', '_', '_', '_', '_'],
    #     ['_', '_', '_', '_', '_', '_', '_'],
    #     ['_', '_', '_', '_', '_', '_', '_'],
    #     ['_', '_', '_', '_', '_', '_', '_']
    # ]
    board = [
        ['_', '_', '_', '_', '_', '_', '_'],
        ['x', 'o', 'x', 'o', 'x', 'o', 'x'],
        ['o', 'o', 'x', 'x', 'o', 'x', 'o'],
        ['x', 'x', 'x', 'o', 'o', 'o', 'x'],
        ['o', 'o', 'o', 'x', 'x', 'x', 'o'],
        ['x', 'x', 'x', 'o', 'x', 'o', 'x']
    ]
    return board
import sys
def printBoard(boardState):
    for i in range(6):
        for j in range(7):
            sys.stdout.write(boardState[i][j])
        print("")

gameState = getBoard()
moveState = [5, 5, 5, 5, 5, 5, 5]
# while True:
#     print("Input 1st player")
#     column = int(input("What is your move? (Choose from 1 to 7)"))
#     gameState[5 - moveState[column - 1]][column-1] = 'x'
#     moveState[column - 1]+= 1
#     printBoard(gameState)
#     score = WinningState(gameState)
#     if score == 1000:
#         print("Player 1 win")
#         break
#
#     print("Input 2nd player")
#     column = int(input("What is your move? (Choose from 1 to 7)"))
#     gameState[5 - moveState[column - 1]][column - 1] = 'o'
#     moveState[column - 1]+= 1
#     printBoard(gameState)
#     score = WinningState(gameState)
#     if score == -1000:
#         print("Player 2 win")
#         break

value = WinningState(gameState)
print(value)