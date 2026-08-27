import sys
import random

# 五子棋
BOARD_ROW = 15
Board = []


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
    if incheck is None:
        return False
    x_check, y_check = incheck.split(sep=",")
    x = int(x_check)
    y = int(y_check)
    if Board[x - 1][y - 1] != '-':
        print("该位置已有棋子，请重新输入")
        return False
    Board[x - 1][y - 1] = check
    check_win(x, y, check)
    return True


def ai_inputCheck(check, x, y):
    if Board[int(x) - 1][int(y) - 1] == '-':
        Board[int(x) - 1][int(y) - 1] = check
        check_win(int(x), int(y), check)
        return True
    return False

# 判断是否五子连珠
def check_win(x, y, check):
    r = x - 1
    c = y - 1
    for dr, dc in ((0, 1), (1, 0), (1, 1), (1, -1)):
        count = 1
        nr, nc = r + dr, c + dc
        while 0 <= nr < BOARD_ROW and 0 <= nc < BOARD_ROW and Board[nr][nc] == check:
            count += 1
            nr += dr
            nc += dc
        nr, nc = r - dr, c - dc
        while 0 <= nr < BOARD_ROW and 0 <= nc < BOARD_ROW and Board[nr][nc] == check:
            count += 1
            nr -= dr
            nc -= dc
        if count >= 5:
            printboard()
            print(check, end="")
            print("胜利，结束")
            sys.exit()

def aiD(x,y):
    num=0
    x1=x+1
    x2=x+2
    x3=x+3
    x4=x+4
    if (x1<15 and x2<15 and x3<15 and x4<15 and y>=0 and x>=0):
        if (Board[x1][y]=="#"):
            num+=1
        if (Board[x2][y]=="#"):
            num+=1
        if (Board[x3][y]=="#"):
            num+=1
        if (Board[x4][y]=="#"):
            num+=1
    return num

def aiA(x,y):
    num=0
    x1=x-1
    x2=x-2
    x3=x-3
    x4=x-4
    if (x1>0 and x2>0 and x3>0 and x4>0 and y>=0 and x>=0):
        if (Board[x1][y]=="#"):
            num+=1
        if (Board[x2][y]=="#"):
            num+=1
        if (Board[x3][y]=="#"):
            num+=1
        if (Board[x4][y]=="#"):
            num+=1
    return num

def aiW(x,y):
    num=0
    y1=y-1
    y2=y-2
    y3=y-3
    y4=y-4
    if (y1>0 and y2>0 and y3>0 and y4>0  and y>=0 and x>=0):
        if (Board[x][y1]=="#"):
            num+=1
        if (Board[x][y2]=="#"):
            num+=1
        if (Board[x][y3]=="#"):
            num+=1
        if (Board[x][y4]=="#"):
            num+=1
    return num

def aiS(x,y):
    num=0
    y1=y+1
    y2=y+2
    y3=y+3
    y4=y+4
    if (y1<15 and y2<15 and y3<15 and y4<15  and y>=0 and x>=0):
        if (Board[x][y1]=="#"):
            num+=1
        if (Board[x][y2]=="#"):
            num+=1
        if (Board[x][y3]=="#"):
            num+=1
        if (Board[x][y4]=="#"):
            num+=1
    return num

def aiQ(x,y):
    num=0
    y1=y-1
    y2=y-2
    y3=y+1
    y4=y+2
    x1=x-1
    x2=x-2
    x3=x+1
    x4=x+2
    if (y1>0 and y2>0 and y3<15 and y4<15 and x1>0 and x2>0 and x3<15 and x4<15):
        if (Board[x1][y1]=="#"):
            num+=1
        if (Board[x2][y2]=="#"):
            num+=1
        if (Board[x3][y3]=="#"):
            num+=1
        if (Board[x4][y4]=="#"):
            num+=1
        if (Board[x3][y1]=="#"):
            num+=1
        if (Board[x4][y2]=="#"):
            num+=1
        if (Board[x1][y3]=="#"):
            num+=1
        if (Board[x2][y4]=="#"):
            num+=1
    return num

def ai_drop():
    ai_x=0
    ai_y=0
    num1=0
    for i in range(len(Board)-1):
        for j in range(len(Board[i])-1):
            if Board[i][j] == '-':
                w=aiW(i,j)
                a = aiA(i, j)
                s = aiS(i, j)
                d = aiD(i, j)
                q=aiQ(i,j)
                if num1<a:
                    num1=a
                    ai_x=i
                    ai_y=j
                if num1<s:
                    num1=s
                    ai_x=i
                    ai_y=j
                if num1<w:
                    num1=w
                    ai_x=i
                    ai_y=j
                if num1<d:
                    num1=d
                    ai_x=i
                    ai_y=j
                if num1<q:
                    num1=q
                    ai_x=i
                    ai_y=j

    if(num1!=0):
        ai_inputCheck('*',ai_x+1,ai_y+1)
    else:
        ai_random()
def ai_random():
    while(1):
            x=random.randint(1,15)
            y=random.randint(1,15)
            if(Board[x-1][y-1]=='-'):
                ai_inputCheck('*',x,y)
                break
def match():
    initboard()
    print()
    print("-------五子棋-------------")
    printboard()
    print("#为玩家，*为电脑")
    check = "#"
    while 1:
        if check == "#":
            if inputCheck("#"):
                printboard()
                check = "*"
        else:
            ai_drop()
            printboard()
            check = "#"

    print()
    print("end")
match()