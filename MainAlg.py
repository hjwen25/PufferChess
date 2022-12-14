#A chess algorithm I worked on for the last few months
#The main structure relies on a complete search with some alpha-beta pruning and a static board eval algorithm (the "EvalAlg3" file)

from tensorflow import keras
import chess
import chess.polyglot
import numpy as np
import pandas as pd
from GetFeatures import GetFeatures
EvalAlg = keras.models.load_model("EvalAlg3")
weights=EvalAlg.get_weights()
opening=chess.polyglot.MemoryMappedReader("Goi040121.bin")

dict1 = {
    'P': 1, 'N': 2, 'B': 3, 'R': 4, 'Q': 5, 'K': 6,
    'p': -1, 'n': -2, 'b': -3, 'r': -4, 'q': -5, 'k': -6
}
dict2 = {
    1: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 2: [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    3: [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    4: [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 5: [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    6: [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    -1: [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], -2: [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    -3: [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    -4: [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], -5: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    -6: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    0: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
values = {"p": 10,
          "b": 30,
          "n": 30,
          "q": 90,
          "k": 1000}

board = chess.Board(chess.STARTING_FEN)


def ReFormat(board):
    global dict1, dict2
    board = [dict1[board.piece_at(x).symbol()] if board.piece_at(x) is not None else 0 for x in chess.SQUARES]
    board = [dict2[x] for x in board]
    board.append([board.count(dict2[y]) for y in range(-6, 7) if y != 0])
    return board


def minimax(depth,board,alpha,beta,player):
    if depth==0:
        feature=GetFeatures(board)
        if not player:
            return -(weights[0][1]*feature[1]+weights[0][2]*feature[2]+weights[1][0])
        else:
            return weights[0][1] * feature[1] + weights[0][2] * feature[2] + weights[1][0]

    moves=list(board.generate_legal_moves())
    if not len(moves):
        if(board):
            return -9999
        return 0
    eval = -9999
    for x in range(len(moves)):
        board.push(moves[x])
        eval = -minimax(depth - 1, board,-beta,-alpha,not player)
        board.pop()
        if eval>=beta:
            return beta
        alpha=max(alpha,eval)
    return eval

def FindMoves(board, depth):
    c=0
    global values, EvalAlg,opening
    try:
        return opening.find(board).move
    except:
        c=0
    moves = list(board.generate_legal_moves())
    good=[]
    for x in range(len(moves)):
        move=moves[x]
        board.push(move)
        c+=1
        print(c)
        good.append(minimax(depth,board,-99999,99999,depth%2))
        board.pop()
    index = np.argmin(good)
    print(np.min(good))
    return moves[index]


def Print(board):
    lists = []
    for piece in reversed(chess.SQUARES):
        lists.append(piece)
    for x in range(8):
        for y in range(7, -1, -1):
            if board.piece_at(lists[x * 8 + y]) != None:
                print(board.piece_at(lists[x * 8 + y]).unicode_symbol(), end=" ")
            else:
                print(".", end=" ")
        print()


def Play(board):
    turn = False
    while True:
        Print(board)
        if turn:
            board.push(FindMoves(board, 3))
        else:
            while True:
                move = input("Enter move: ")
                try:
                    board.push_san(move)
                    break
                except:
                    continue
        if not bool(board.legal_moves):
            Print(board)
            return 0
        print()
        turn = not turn

Play(board)
