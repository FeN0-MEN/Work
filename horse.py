import numpy as np

f = open("input.txt", "r", encoding="utf-8")

heigth, widtg = f.read(3).split(' ')
b = f.readlines(2)
statX, startY = b[-1].split(' ')

heigth = int(heigth)
widtg = int(widtg)
startX = heigth - int(statX)
startY = int(startY) - 1

board = np.zeros((heigth, widtg), dtype=int)
f.close()


def BestWay(X, Y, board, currentStep=1):
    if X < 0 or X >= len(board):
        return False
    if Y < 0 or Y >= len(board[0]):
        return False
    if board[X, Y] != 0:
        return False

    board[X, Y] = currentStep
    if (len(board[board == 0]) == 0):
        return True
    NewStep = currentStep + 1

    def NextStep(X, Y, znach):
        variants = {
            0: lambda X, Y: (X + 1, Y + 2),
            1: lambda X, Y: (X + 2, Y + 1),
            2: lambda X, Y: (X + 2, Y - 1),
            3: lambda X, Y: (X + 1, Y - 2),
            4: lambda X, Y: (X - 1, Y - 2),
            5: lambda X, Y: (X - 2, Y - 1),
            6: lambda X, Y: (X - 2, Y + 1),
            7: lambda X, Y: (X - 1, Y + 2),
        }
        return variants[znach](X, Y)

    for i in range(8):
        NewX, NewY = NextStep(X, Y, i)
        if BestWay(NewX, NewY, board, NewStep) == True:
            return True
    else:
        board[X, Y] = 0
        return False


usl = BestWay(startX, startY, board)
f = open('output.txt', 'w', encoding='utf8')

if usl == True:
    f.write(str(board))
else:
    f.write( 'Правильный маршрут не найден' )
f.close()
