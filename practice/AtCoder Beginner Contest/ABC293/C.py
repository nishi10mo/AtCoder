# Make Takahashi Happy
from itertools import permutations
def f(H, W, A):
    visited = set([A[0][0]])
    def search_board(h, w, board, visited, b_x, b_y):
        if b_x == h-1 and b_y == w-1:
            return 1
        else:
            ret = 0
            if b_x != h-1 and board[b_x+1][b_y] not in visited:
                visited.add(board[b_x+1][b_y])
                ret += search_board(h, w, board, visited, b_x+1, b_y)
                visited.remove(board[b_x+1][b_y])
            if b_y != w-1 and board[b_x][b_y+1] not in visited:
                visited.add(board[b_x][b_y+1])
                ret += search_board(h, w, board, visited, b_x, b_y+1)
                visited.remove(board[b_x][b_y+1])
        return ret
    return search_board(H, W, A, visited, 0, 0)

def main():
    H, W = [int(i) for i in input().split()]
    A = []
    for _ in range(H):
        a = [int(i) for i in input().split()]
        A.append(a)
    print(f(H, W, A))

if __name__=="__main__":
    main()