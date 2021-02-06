import sys
import pygame
import math

opp = 0
def Minimax(gameState, isMaximizer, availableMoveRow, alpha, beta, depth): # availableMoveRow - row where we can give the next move
    remainingMoves = 7
    for i in range(7):
        if gameState[0][i] != 0:
            remainingMoves -= 1

    isWinningStase = WinningState(gameState)
    if remainingMoves == 0 or depth == 0 or isWinningStase:
        if isWinningStase == 1000:
            return None, 1000 - (6 - depth)
        elif isWinningStase == -1000:
            return None, -1000 + (6 - depth)
        else:
            score = evaluateScore(boardState)
            # print(score)
            return None, score
    if isMaximizer:
        bestScore = alpha
        bestColumn = 0
        for i in range(7):
            if gameState[0][i] == 0:
                gameState[5 - availableMoveRow[i]][i] = 2
                # print(gameState)
                availableMoveRow[i]+=1
                col, score = Minimax(gameState, not isMaximizer, availableMoveRow, alpha, beta, depth - 1)
                global opp
                opp+= 1
                # print(opp)
                # print(score)
                availableMoveRow[i] -= 1
                gameState[5 - availableMoveRow[i]][i] = 0
                if score > bestScore:
                    bestScore = score
                    bestColumn = i
                bestScore = max(bestScore, score)
                alpha = max(bestScore, alpha)
                if beta <= alpha:
                    break
        # print(bestScore)
        # print(bestColumn)
        # print(opp)
        return bestColumn, bestScore

    else:
        bestScore = beta
        bestColumn = 0
        for i in range(7):
            if gameState[0][i] == 0:
                gameState[5 - availableMoveRow[i]][i] = 1
                # print(gameState)
                availableMoveRow[i]+=1
                col, score = Minimax(gameState, not isMaximizer, availableMoveRow, alpha, beta, depth - 1)
                # print(score)
                opp+= 1
                # print(opp)
                availableMoveRow[i] -= 1
                gameState[5 - availableMoveRow[i]][i] = 0
                if score < bestScore:
                    bestScore = score
                    bestColumn = i
                bestScore = min(bestScore, score)
                beta = min(bestScore, beta)
                if alpha >= beta:
                    break
        # print(bestScore)
        # print(bestColumn)
        # print(opp)
        return bestColumn, bestScore
    # return boardState


def printBoard(boardState):
    for i in range (6):
        for j in range (7):
            if boardState[i][j] == 0:
                sys.stdout.write('_')
            elif boardState[i][j] == 1:
                sys.stdout.write('o')
            else:
                sys.stdout.write('x')
        print("")


def WinningState(gameState):
    totalInARow = 0
    # x-axis check
    for i in range(6):
        totalInARow = 0
        for j in range(7 - 1):
            if gameState[5 - i][j] == 2:
                if gameState[5 - i][j + 1] == 2 and totalInARow < 4:  # array index out of bound
                    totalInARow += 1
                    if totalInARow == 3:
                        totalInARow += 1
                        return 1000
                else:
                    totalInARow = 0

            elif gameState[5 - i][j] == 1:
                if gameState[5 - i][j + 1] == 1 and totalInARow < 4:
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
            if gameState[5 - j][i] == 2:
                if gameState[5 - j - 1][i] == 2 and totalInARow < 4:  # array index out of bound
                    totalInARow += 1
                    if totalInARow == 3:
                        totalInARow += 1
                        return 1000
                else:
                    totalInARow = 0

            elif gameState[5 - j][i] == 1:
                if gameState[5 - j - 1][i] == 1 and totalInARow < 4:
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
                if gameState[r + k][c + k] == 2:
                    if gameState[r + k + 1][c + k + 1] == 2:
                        totalInARow += 1
                        if totalInARow == 3:
                            totalInARow += 1
                            return 1000
                    else:
                        totalInARow = 0

                # totalInARow = 0

                elif gameState[r + k][c + k] == 1:
                    if gameState[r + k + 1][c + k + 1] == 1:
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
                if gameState[r - k][c + k] == 2:
                    totalInARow += 1
                else:
                    totalInARow = 0
                if totalInARow == 4:
                    return 1000
            totalInARow = 0
            for k in range(4):
                if gameState[r - k][c + k] == 1:
                    totalInARow += 1
                else:
                    totalInARow = 0
                if totalInARow == 4:
                    return -1000
            totalInARow = 0

    return 0

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

def evaluateScore(boardState):
    evalX = 0
    huristics = getHuristicTable()
    for i in range(6):
        for j in range(7):
            if boardState[i][j] == 2:
                evalX+= huristics[i][j]
            elif boardState[i][j] == 1:
                evalX-= huristics[i][j]

    return evalX


# def evaluateScore(boardState, isMaximizer):
#     evalX = 0
#     huristics = getHuristicTable()
#     if isMaximizer:
#         for i in range(6):
#             for j in range(7):
#                 if boardState[i][j] == 'x':
#                     evalX+= huristics[i][j]
#                 elif boardState[i][j] == 'o':
#                     evalX-= huristics[i][j]
#     else:
#         for i in range(6):
#             for j in range(7):
#                 if boardState[i][j] == 'x':
#                     evalX+= huristics[i][j]
#                 elif boardState[i][j] == 'o':
#                     evalX-= huristics[i][j]
#     return evalX

def getBoard():
    # board = [
    #     ['x', 'o', 'x', 'x', 'x', 'o', 'x'],
    #     ['o', 'x', 'x', 'o', 'o', 'x', 'o'],
    #     ['o', 'o', 'o', 'x', 'x', 'o', 'x'],
    #     ['x', 'x', 'x', 'o', 'o', 'x', 'o'],
    #     ['o', 'o', 'o', 'x', 'x', 'o', 'x'],
    #     ['x', 'o', 'o', 'o', 'x', 'x', 'o']
    # ]
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    return board

def matchDraw(gameState):
    availableColumn = 7
    for i in range(7):
        if gameState[0][i] != 0:
            availableColumn-= 1
    if availableColumn == 0:
        return True
    else:
        return False


def draw_board(board):
    for r in range(6):
        for c in range(7):
            pygame.draw.rect(screen, (0, 0, 255), (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, (0, 0, 0), (
            int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for r in range(6):
        for c in range(7):
            if board[r][c] == 1:
                pygame.draw.circle(screen, (255, 0, 0), (
                int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, (255, 255, 0), (
                int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


boardState = getBoard()
alpha = -10000000
beta = 10000000

moveState = [0, 0, 0, 0, 0, 0, 0]
# moveState = [5, 5, 5, 6, 2, 0, 0]


pygame.init()
SQUARESIZE = 70

width = 7 * SQUARESIZE
height = (6+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(boardState)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 45)

turn = 0
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            pygame.draw.circle(screen, (255, 0, 0), (posx, int(SQUARESIZE / 2)), RADIUS)

        pygame.display.update()


        if matchDraw(boardState):
            print("Match Draw!!!!")
            break
        else:
            if event.type == pygame.MOUSEBUTTONUP:
                print("sami")
                print(event.pos)
                pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, SQUARESIZE))
                if turn == 0:
                    turn = 1
                    posx = event.pos[0]
                    print(posx)

                    # pygame.display.update()

                    print("Input 1st player")
                    column = int(math.floor(posx/SQUARESIZE))
                    boardState[5 - moveState[column]][column] = 1
                    moveState[column]+= 1
                    printBoard(boardState)
                    draw_board(boardState)
                    score = WinningState(boardState)
                    if score <= -990:
                        label = myfont.render("You Win!!", 1, (255, 0, 0))
                        screen.blit(label, (40, 10))
                        print("Player 1 win")
                        pygame.display.update()
                        pygame.time.wait(5000)
                        break

    # if matchDraw(boardState):
    #     print("Match Draw!!!!")
    #     break
    # else:
    #     print("Input 1st player")
    #     column, score = Minimax(boardState, False, moveState, alpha, beta, 8)
    #     print(column)
    #     boardState[5 - moveState[column]][column] = 'o'
    #     moveState[column] += 1
    #     printBoard(boardState)
    #     score = WinningState(boardState)
    #     print(score)
    #     if score == -1000:
    #         print("Player 1 win")
    #         break
    if turn == 1:
        turn = 0
        if matchDraw(boardState):
            print("Match Draw!!!")
            break
        else:
            print("Input 2nd player")
            column, score = Minimax(boardState, True, moveState, alpha, beta, 6)
            print(column)
            boardState[5 - moveState[column]][column] = 2
            moveState[column]+= 1
            printBoard(boardState)
            draw_board(boardState)
            score = WinningState(boardState)
            if score >= 990:
                label = myfont.render("Computer wins!!", 1, (255, 255, 0))
                screen.blit(label, (40, 10))
                print("Player 2 win")
                pygame.display.update()
                pygame.time.wait(5000)
                break


value = WinningState(boardState)
print(value)

