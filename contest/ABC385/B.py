# Santa Claus 1
def f(H, W, X, Y, S, T):
    x = X-1
    y = Y-1
    house = set()
    for t in T:
        pre_x = x
        pre_y = y
        if t == "U":
            x -= 1
        elif t == "D":
            x += 1
        elif t == "L":
            y -= 1
        elif t == "R":
            y += 1
        if S[x][y] == "#":
            x = pre_x
            y = pre_y
        elif S[x][y] == ".":
            pass
        else:
            house.add((x, y))
    n = len(house)
    return [x+1, y+1, n]

def main():
    H, W, X, Y = [int(i) for i in input().split()]
    S = []
    for _ in range(H):
        S.append(list(input()))
    T = list(input())
    print(*f(H, W, X, Y, S, T))

if __name__ == '__main__':
    main()
