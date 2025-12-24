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
            if check == "#":
                wide1.append(int(x_check))
                high1.append(int(y_check))
                if len(wide1) >= 5:
                    for i in range(len(wide1)):
                        if (wide1[i] + int(y_check)) / (high1[i] + int(x_check)) == 1:
                            num1.append(wide1[i])
                            win(num1, "#")
                        if wide1[i] == int(x_check):
                            num11.append(high1[i])
                            win(num11, "#")
                        if high1[i] == int(y_check):
                            num12.append(wide1[i])
                            win(num12, "#")
                    num1.clear()
                    num11.clear()
                    num12.clear()
                return True