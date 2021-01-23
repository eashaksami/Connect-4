import sys
opp = 0
def Minimax(gameState, isMaximizer, availableMoveRow, alpha, beta, depth): # availableMoveRow - row where we can give the next move
    remainingMoves = 7
    for i in range(7):
        if gameState[0][i] != '_':
            remainingMoves -= 1

    if remainingMoves == 0 or depth == 0:
        if WinningState(gameState) == 1000:
            return None, 1000
        elif WinningState(gameState) == -1000:
            return None, -1000
        else:
            score = evaluateScore(boardState, isMaximizer)
            # print(score)
            return None, score
    if isMaximizer:
        bestScore = alpha
        bestColumn = 0
        for i in range(7):
            if gameState[0][i] == '_':
                gameState[5 - availableMoveRow[i]][i] = 'x'
                # print(gameState)
                availableMoveRow[i]+=1
                col, score = Minimax(gameState, not isMaximizer, availableMoveRow, alpha, beta, depth - 1)
                global opp
                # print(opp)
                # print(score)
                availableMoveRow[i] -= 1
                gameState[5 - availableMoveRow[i]][i] = '_'
                if score > bestScore:
                    bestScore = score
                    bestColumn = i
                bestScore = max(bestScore, score)
                alpha = max(bestScore, alpha)
                if beta <= alpha:
                    break
        # print(bestScore)
        # print(bestColumn)
        return bestColumn, bestScore

    else:
        bestScore = beta
        bestColumn = 0
        for i in range(7):
            if gameState[0][i] == '_':
                gameState[5 - availableMoveRow[i]][i] = 'o'
                # print(gameState)
                availableMoveRow[i]+=1
                col, score = Minimax(gameState, not isMaximizer, availableMoveRow, alpha, beta, depth - 1)
                # print(score)
                opp+= 1
                # print(opp)
                availableMoveRow[i] -= 1
                gameState[5 - availableMoveRow[i]][i] = '_'
                if score < bestScore:
                    bestScore = score
                    bestColumn = i
                bestScore = min(bestScore, score)
                beta = min(bestScore, beta)
                if alpha >= beta:
                    break
        # print(bestScore)
        # print(bestColumn)
        return bestColumn, bestScore
    # return boardState


def printBoard(boardState):
    for i in range (6):
        for j in range (7):
            sys.stdout.write(boardState[i][j])
        print("")


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
                        totalInARow += 1
                        if totalInARow == 3:
                            totalInARow += 1
                            return 1000
                    else:
                        totalInARow = 0

                # totalInARow = 0

                elif gameState[r + k][c + k] == 'o':
                    if gameState[r + k + 1][c + k + 1] == 'o':
                        totalInARow += 1
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
                    totalInARow += 1
                else:
                    totalInARow = 0
                if totalInARow == 4:
                    return 1000
            totalInARow = 0
            for k in range(4):
                if gameState[r - k][c + k] == 'o':
                    totalInARow += 1
                else:
                    totalInARow = 0
                if totalInARow == 4:
                    return -1000
            totalInARow = 0

    return 1

def Evaluate():
    pass
def getHuristicTable():
    hursitics = [
        [3, 4, 5, 7, 5, 4, 3],
        [4, 6, 8, 10, 8, 6, 4],
        [5, 8, 11, 13, 11, 8, 5],
        [5, 8, 11, 13, 11, 8, 5],
        [4, 6, 8, 10, 8, 6, 4],
        [3, 4, 5, 7, 5, 4, 3]
    ]
    return hursitics

def evaluateScore(boardState, isMaximizer):
    evalX = 0
    evalY = 0
    huristics = getHuristicTable()
    for i in range(6):
        for j in range(7):
            if boardState[i][j] == 'x':
                evalX+= huristics[i][j]
            elif boardState[i][j] == 'o':
                evalY+= huristics[i][j]
    if isMaximizer:
        return evalX
    else:
        print("isMaximizer is false")
        evalY*= -1
        return evalY

def getBoard():
    # board = [
    #     ['x', 'o', '_', '_', '_', 'o', 'o'],
    #     ['o', 'o', '_', 'x', 'o', 'o', 'o'],
    #     ['o', 'x', 'o', 'o', 'x', 'o', 'o'],
    #     ['o', 'x', 'x', 'o', 'x', 'x', 'x'],
    #     ['x', 'o', 'x', 'o', 'x', 'x', 'o'],
    #     ['x', 'o', 'x', 'x', 'o', 'x', 'x']
    # ]
    board = [
        ['_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_']
    ]
    return board

boardState = getBoard()
alpha = -10000000
beta = 10000000

moveState = [0, 0, 0, 0, 0, 0, 0]
while True:
    print("Input 1st player")
    column = int(input("What is your move? (Choose from 1 to 7)"))
    boardState[5 - moveState[column - 1]][column-1] = 'x'
    moveState[column - 1]+= 1
    printBoard(boardState)
    score = WinningState(boardState)
    if score == 1000:
        print("Player 1 win")
        break

    print("Input 2nd player")
    column, score = Minimax(boardState, True, moveState, alpha, beta, 4)
    boardState[5 - moveState[column]][column] = 'o'
    moveState[column]+= 1
    printBoard(boardState)
    score = WinningState(boardState)
    if score == -1000:
        print("Player 2 win")
        break

value = WinningState(boardState)
print(value)


# board = [
#         ['_', '_', '_', '_', '_', '_', '_'],
#         ['_', '_', '_', '_', '_', '_', '_'],
#         ['_', '_', '_', '_', '_', '_', '_'],
#         ['_', '_', '_', '_', '_', '_', '_'],
#         ['o', 'o', '_', '_', '_', '_', '_'],
#         ['x', 'x', '_', 'x', '_', '_', '_']
# ]


# print(evalX)
# print(evalY)
