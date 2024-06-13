# Divide and Divide
# import math

# def calc(board):
#     ans = 0
#     flag = False
#     for i in board:
#         if i >= 2:
#             board.remove(i)
#             x1 = math.floor(i/2)
#             x2 = math.ceil(i/2)
#             board.append(x1)
#             board.append(x2)
#             ans += i
#             flag = True
#     return board, ans, flag    

from functools import cache

@cache
def f(N):
    return 0 if N==1 else f(N//2) + f((N+1)//2) + N

def main():
    N = int(input())
    print(f(N))

if __name__=="__main__":
    main()
