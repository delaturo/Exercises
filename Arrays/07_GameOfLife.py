import copy
def gameOfLife(board):
    lastGen = copy.deepcopy(board)
    i=0
    while( i < len(lastGen)):
        j = 0
        while (j < len(lastGen[i])):
            board[i][j] = shouldBeAlive(lastGen,i,j)
            j += 1
        i += 1

def shouldBeAlive(board,i,j):
    ii = i-1
    sum = 0
    while (ii <= i+1):
        if ii >= 0  and ii < len(board):
            jj = j-1
            while (jj <= j+1):
                if jj >= 0  and jj < len(board[i]) and (ii != i or jj != j):
                    if board[ii][jj]:
                        sum += 1
                jj += 1
        ii += 1
    return 1 if ((board[i][j] and sum >=2 and sum <= 3) or sum == 3) else 0



def createInput():
    return [[[0,1,0],[0,0,1],[1,1,1],[0,0,0]],
        [[1,1],[1,0]]
    ]
    # return [[1,1],[1,0]]



N = createInput()
for n in N:
    print("=========================")
    print(n)
    gameOfLife(n)
    print(n)
    print("=========================")