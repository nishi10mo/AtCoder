# Bombs
import copy
def f(R, C, B):
    def bomb(i, j, b, impact):
        for x in range(impact+1):
            for y in range(impact+1-x):
                if i - x >= 0:
                    if j - y >= 0:
                        if b[i-x][j-y] == "#":
                            b[i-x][j-y] = "."
                    if j + y < C:
                        if b[i-x][j+y] == "#":
                            b[i-x][j+y] = "."
                if i + x < R:
                    if j - y >= 0:
                        if b[i+x][j-y] == "#":
                            b[i+x][j-y] = "."
                    if j + y < C:
                        if b[i+x][j+y] == "#":
                            b[i+x][j+y] = "."
        return b
    b = copy.deepcopy(B)
    for i in range(R):
        for j in range(C):
            if b[i][j] != "." and b[i][j] != "#":
                b = bomb(i, j, b, int(b[i][j]))
                b[i][j] = "."
    return b

def main():
    R, C = [int(i) for i in input().split()]
    B = []
    for _ in range(R):
        B.append(list(input()))
    B = f(R, C, B)
    for b in B:
        print("".join(b))

if __name__ == '__main__':
    main()
