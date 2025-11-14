import sys
# 五子棋
BOARD_ROW = 15
Board = []
high = []
wide = []
num = []
num1 = []
num2 = []


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
            wide.append(int(x_check))
            high.append(int(y_check))
            if len(wide) >= 5:
                for i in range(len(wide)):
                    if (wide[i] + int(y_check)) / (high[i] + int(x_check)) == 1:
                        num.append(wide[i])
                        sorts(num)
                    if wide[i] == int(x_check):
                        num1.append(high[i])
                        sorts(num1)
                    if high[i] == int(y_check):
                        num2.append(wide[i])
                        sorts(num2)
                num.clear()
                num1.clear()
                num2.clear()
            return True
        else:
            print("error")
            return False


# 判断五位数字是否相连
def sorts(num):
    num.sort()
    n = 0
    j = 0
    n = num[0]
    for i in num:
        if i == n:
            n = i + 1
            j = j + 1
            if j >= 5:
                printboard()
                print('成功')
                sys.exit()
        else:
            n = i
            n = n + 1
            j = 1

#def ai_drop():


def match():
    initboard()
    print()
    print("-------五子棋-------------")
    printboard()
    check = "#"
    while 1:
        if check == "#":
            same = inputCheck("#")
            printboard()
            check = "*"

        elif check == "*":
            same = inputCheck("*")
            printboard()
            check = "#"
        else:
            break

    print()
    print("end")


match()
