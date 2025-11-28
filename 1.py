import sys
import random

# 五子棋
BOARD_ROW = 15
Board = []
high1 = []
wide1 = []
num1 = []
num11 = []
num12 = []
high2 = []
wide2 = []
num2 = []
num21 = []
num22 = []


def initboard():
    for i in range(BOARD_ROW):
        row = ["-"] * BOARD_ROW
        Board.append(row)


def printboard():
    print()
    for i in range(len(Board)):
        for j in range(len(Board[i])):
            print(Board[i][j], end=" ")
        print()

def inputCheck(check):
    incheck = input("请输入你的棋子,格式为x,y")
    if incheck is not None:
        x_check, y_check = incheck.split(sep=",")
        if Board[int(x_check) - 1][int(y_check) - 1] == '-':
            Board[int(x_check) - 1][int(y_check) - 1] = check