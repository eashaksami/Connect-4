import sys
opp = 0
def Minimax(gameState, isMaximizer, availableMoveRow, alpha, beta): # availableMoveRow - row where we can give the next move
    remainingMoves = 7
    for i in range(7):
        if gameState[0][i] != '_':
            remainingMoves -= 1
    if remainingMoves == 0:
        score = WinningState(gameState)
        return score
    if isMaximizer:
        bestScore = alpha
        for i in range(7):
            if gameState[0][i] == '_':
                gameState[5 - availableMoveRow[i]][i] = 'x'
                # print(gameState)
                availableMoveRow[i]+=1
                score = Minimax(gameState, not isMaximizer, availableMoveRow, alpha, beta)
                global opp
                opp+= 1
                print(opp)
                # print(score)
                availableMoveRow[i] -= 1
                gameState[5 - availableMoveRow[i]][i] = '_'
                bestScore = max(bestScore, score)
                alpha = max(bestScore, alpha)
                if beta <= alpha:
                    break
        return bestScore

    else:
        bestScore = beta
        for i in range(7):
            if gameState[0][i] == '_':
                gameState[5 - availableMoveRow[i]][i] = 'o'
                # print(gameState)
                availableMoveRow[i]+=1
                score = Minimax(gameState, not isMaximizer, availableMoveRow, alpha, beta)
                # print(score)
                opp+= 1
                print(opp)
                availableMoveRow[i] -= 1
                gameState[5 - availableMoveRow[i]][i] = '_'
                bestScore = min(bestScore, score)
                beta = min(bestScore, beta)
                if alpha >= beta:
                    break
        return bestScore
    return boardState


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

def getBoard():
    # board = [
    #     ['x', 'o', '_', '_', '_', 'o', 'o'],
    #     ['o', 'o', '_', 'x', 'o', 'o', 'o'],
    #     ['o', 'x', 'o', 'o', 'x', 'o', 'o'],
    #     ['o', 'x', 'x', 'o', 'x', 'x', 'x'],
    #     ['o', 'o', 'x', 'o', 'o', 'x', 'x'],
    #     ['x', 'o', 'x', 'x', 'o', 'x', 'x']
    # ]
    board = [
        ['_', '_', '_', '_', '_', '_', '_'],
        ['o', 'x', 'o', 'x', 'x', 'o', 'x'],
        ['o', 'o', 'o', 'x', 'x', 'x', 'o'],
        ['x', 'x', 'x', 'o', 'x', 'o', 'x'],
        ['x', 'o', 'x', 'x', 'o', 'o', 'o'],
        ['x', 'x', 'o', 'x', 'o', 'o', 'x']
    ]
    return board

boardState = getBoard()
availableMoves = [5, 5, 5, 5, 5, 5, 5]
alpha = -10000000
beta = 10000000
state = Minimax(boardState, False, availableMoves, alpha, beta)
print("in main")
print(state)