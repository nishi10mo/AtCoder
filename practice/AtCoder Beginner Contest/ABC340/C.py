# Divide and Divide
import math

def calc(board):
    ans = 0
    flag = False
    for i in board:
        if i >= 2:
            board.remove(i)
            x1 = math.floor(i/2)
            x2 = math.ceil(i/2)
            board.append(x1)
            board.append(x2)
            ans += i
            flag = True
    return board, ans, flag        

def main():
    N = int(input())
    board = [N]
    flag = True
    ans = 0
    while flag == True:
        board, ans_, flag = calc(board)
        ans += ans_
    print(ans)

if __name__=="__main__":
    main()
