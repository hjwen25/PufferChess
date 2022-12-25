#Feature extraction with the use of a piece square table

import chess
value = {0: 0,
         1: 100, -1: -100,
         2: 320, -2: -320,
         3: 330, -3: -330,
         4: 500, -4: -500,
         5: 900, -5: -900,
         6: 20000, -6: -20000}

convert = {
    'P': 1, 'N': 2, 'B': 3, 'R': 4, 'Q': 5, 'K': 6,
    'p': -1, 'n': -2, 'b': -3, 'r': -4, 'q': -5, 'k': -6
}
WP=[ 0,  0,  0,  0,  0,  0,  0,  0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
     5,  5, 10, 25, 25, 10,  5,  5,
     0,  0,  0, 20, 20,  0,  0,  0,
     5, -5,-10,  0,  0,-10, -5,  5,
     5, 10, 10,  1,  1, 10, 10,  5,
     0,  0,  0,  0,  0,  0,  0,  0]

BP=[ 0,  0,  0,  0,  0,  0,  0,  0,
     5, 10, 10,  1,  1, 10, 10,  5,
     5, -5,-10,  0,  0,-10, -5,  5,
     0,  0,  0, 20, 20,  0,  0,  0,
     5,  5, 10, 25, 25, 10,  5,  5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
     0,  0,  0,  0,  0,  0,  0,  0]

WN=[-50,-40,-30,-30,-30,-30,-40,-50,
    -40,-20,  0,  0,  0,  0,-20,-40,
    -30,  0, 10, 15, 15, 10,  0,-30,
    -30,  5, 15, 20, 20, 15,  5,-30,
    -30,  0, 15, 20, 20, 15,  0,-30,
    -30,  5, 10, 15, 15, 10,  5,-30,
    -40,-20,  0,  5,  5,  0,-20,-40,
    -50,-40,-30,-30,-30,-30,-40,-50]

BN=[-50,-40,-30,-30,-30,-30,-40,-50,
    -40,-20,  0,  5,  5,  0,-20,-40,
    -30,  5, 10, 15, 15, 10,  5,-30,
    -30,  0, 15, 20, 20, 15,  0,-30,
    -30,  5, 15, 20, 20, 15,  5,-30,
    -30,  0, 10, 15, 15, 10,  0,-30,
    -40,-20,  0,  0,  0,  0,-20,-40,
    -50,-40,-30,-30,-30,-30,-40,-50]

WB=[-20,-10,-10,-10,-10,-10,-10,-20,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -10,  0,  5, 10, 10,  5,  0,-10,
    -10,  5,  5, 10, 10,  5,  5,-10,
    -10,  0, 10, 10, 10, 10,  0,-10,
    -10, 10, 10, 10, 10, 10, 10,-10,
    -10,  5,  0,  0,  0,  0,  5,-10,
    -20,-10,-10,-10,-10,-10,-10,-20]

BB=[-20,-10,-10,-10,-10,-10,-10,-20,
    -10,  5,  0,  0,  0,  0,  5,-10,
    -10, 10, 10, 10, 10, 10, 10,-10,
    -10,  0, 10, 10, 10, 10,  0,-10,
    -10,  5,  5, 10, 10,  5,  5,-10,
    -10,  0,  5, 10, 10,  5,  0,-10,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -20,-10,-10,-10,-10,-10,-10,-20]

WR=[  0,  0,  0,  0,  0,  0,  0,  0,
      5, 10, 10, 10, 10, 10, 10,  5,
     -5,  0,  0,  0,  0,  0,  0, -5,
     -5,  0,  0,  0,  0,  0,  0, -5,
     -5,  0,  0,  0,  0,  0,  0, -5,
     -5,  0,  0,  0,  0,  0,  0, -5,
     -5,  0,  0,  0,  0,  0,  0, -5,
      0,  0,  5,  6,  6,  5,  0,  0]

BR=[  0,  0,  5,  6,  6,  5,  0,  0,
     -5,  0,  0,  0,  0,  0,  0, -5,
     -5,  0,  0,  0,  0,  0,  0, -5,
     -5,  0,  0,  0,  0,  0,  0, -5,
     -5,  0,  0,  0,  0,  0,  0, -5,
     -5,  0,  0,  0,  0,  0,  0, -5,
      5, 10, 10, 10, 10, 10, 10,  5,
      0,  0,  0,  0,  0,  0,  0,  0]

WQ=[-20,-10,-10, -5, -5,-10,-10,-20,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -10,  0,  5,  5,  5,  5,  0,-10,
     -5,  0,  5,  5,  5,  5,  0, -5,
      0,  0,  5,  5,  5,  5,  0, -5,
    -10,  5,  5,  5,  5,  5,  0,-10,
    -10,  0,  5,  0,  0,  0,  0,-10,
    -20,-10,-10, -5, -5,-10,-10,-20]

BQ=[-20,-10,-10, -5, -5,-10,-10,-20,
    -10,  0,  5,  0,  0,  0,  0,-10,
    -10,  5,  5,  5,  5,  5,  0,-10,
      0,  0,  5,  5,  5,  5,  0, -5,
     -5,  0,  5,  5,  5,  5,  0, -5,
    -10,  0,  5,  5,  5,  5,  0,-10,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -20,-10,-10, -5, -5,-10,-10,-20,]

WK1=[-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-20,-30,-30,-40,-40,-30,-30,-20,
-10,-20,-20,-20,-20,-20,-20,-10,
 20, 20,  0,  0,  0,  0, 20, 20,
 20, 30, 10,  0,  0, 10, 30, 20]

WK2=[-50,-40,-30,-20,-20,-30,-40,-50,
-30,-20,-10,  0,  0,-10,-20,-30,
-30,-10, 20, 30, 30, 20,-10,-30,
-30,-10, 30, 40, 40, 30,-10,-30,
-30,-10, 30, 40, 40, 30,-10,-30,
-30,-10, 20, 30, 30, 20,-10,-30,
-30,-30,  0,  0,  0,  0,-30,-30,
-50,-30,-30,-30,-30,-30,-30,-50]

def BishopMobility(board, i, j):
    mobility = 0
    for x in range(1, 8):
        if i + x > 7 or j + x > 7 or board[i + x][j + x] != 0:
            break
        mobility += 1
    for x in range(1, 8):
        if i - x < 0 or j - x < 0 or board[i - x][j - x] != 0:
            break
        mobility += 1
    for x in range(1, 8):
        if i + x > 7 or j - x < 0 or board[i + x][j - x] != 0:
            break
        mobility += 1
    for x in range(1, 8):
        if i - x < 0 or j + x > 7 or board[i - x][j + x] != 0:
            break
        mobility += 1
    return mobility


def RookMobility(board, i, j):
    mobility = 0
    for x in range(1, 8):
        if i + x > 7 or board[i + x][j] != 0:
            break
        mobility += 1
    for x in range(1, 8):
        if j + x > 7 or board[i][j + x] != 0:
            break
        mobility += 1
    for x in range(1, 8):
        if i - x < 0 or board[i - x][j] != 0:
            break
        mobility += 1
    for x in range(1, 8):
        if j - x < 0 or board[i - x][j] != 0:
            break
        mobility += 1
    return mobility

def GetFeatures(data):
    board=[convert[data.piece_at(y).symbol()] if data.piece_at(y) is not None else 0 for y in chess.SQUARES]
    SideToMove = int(data.turn == chess.BLACK)
    MaterialCount = []
    for y in range(-6, 7):
        if y != 0:
            MaterialCount.append(board.count(y))
    #CastlingRights = [int(data.has_kingside_castling_rights(chess.WHITE)),
    #                  int(data.has_queenside_castling_rights(chess.WHITE)),
    #                  int(data.has_kingside_castling_rights(chess.BLACK)),
    #                  int(data.has_queenside_castling_rights(chess.BLACK))]
    Material = 0
    for y in range(len(MaterialCount)):
        Material += int(value[(y - 6) if y < 6 else (y - 5)] * MaterialCount[y])
    Mobility = [0, 0, 0, 0, 0, 0]

    #Reformat Boards
    reform = []
    for x in range(len(board)):
        if x % 8 == 0:
            reform.append([board[x]])
        else:
            reform[int(x / 8)].append(board[x])

    for i in range(8):
        for j in range(8):
            #White Bishops
            if reform[i][j] == 3:
                Mobility[0] += BishopMobility(reform, i, j)
            #White Rooks
            elif reform[i][j] == 4:
                Mobility[1] += RookMobility(reform, i, j)
            #White Queen(s) (Basically a combination of rook & bishop)
            elif reform[i][j] == 5:
                Mobility[2] += BishopMobility(reform, i, j)
                Mobility[2] += RookMobility(reform, i, j)
            #Black Bishops
            elif reform[i][j] == -3:
                Mobility[3] -= BishopMobility(reform, i, j)
            #Black Rooks
            elif reform[i][j] == -4:
                Mobility[4] -= RookMobility(reform, i, j)
            #Black Queen(s)
            elif reform[i][j] == -5:
                Mobility[2] -= BishopMobility(reform, i, j)
                Mobility[2] -= RookMobility(reform, i, j)
    for x in range(len(board)):
        if board[x]==1:
            Material+=WP[x]
        elif board[x]==2:
            Material+=WN[x]
        elif board[x]==3:
            Material+=WB[x]
        elif board[x]==4:
            Material+=WR[x]
        elif board[x]==5:
            Material+=WQ[x]
        elif board[x]==-1:
            Material-=BP[x]
        elif board[x]==-2:
            Material-=BN[x]
        elif board[x]==-3:
            Material-=BB[x]
        elif board[x]==-4:
            Material-=BR[x]
        elif board[x]==-5:
            Material-=BQ[x]
    #MaterialCount[0],MaterialCount[1],MaterialCount[2],MaterialCount[3],MaterialCount[4],MaterialCount[5],MaterialCount[6],MaterialCount[7],MaterialCount[8],MaterialCount[9],MaterialCount[10],MaterialCount[11]
    return [SideToMove, Material, sum(Mobility)]
