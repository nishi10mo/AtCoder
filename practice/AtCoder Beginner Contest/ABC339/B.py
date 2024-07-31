# Langton's Takahashi
def f(H, W, N):
    def forward(x, y, ori):
        nonlocal H
        nonlocal W
        if ori == "right":
            if x < W-1:
                x += 1
            else:
                x = 0
        elif ori == "down":
            if y < H-1:
                y += 1
            else:
                y = 0
        elif ori == "left":
            if 0 < x:
                x -= 1
            else:
                x = W-1
        else:
            if 0 < y:
                y -= 1
            else:
                y = H-1
        return x, y
    grid = [["."]*W for _ in range(H)]
    ori = "up"
    x = 0
    y = 0
    for i in range(N):
        if grid[y][x] == ".":
            grid[y][x] = "#"
            if ori == "up":
                ori = "right"
            elif ori == "right":
                ori = "down"
            elif ori == "down":
                ori = "left"
            else:
                ori = "up"
            x, y = forward(x, y, ori)
        else:
            grid[y][x] = "."
            if ori == "up":
                ori = "left"
            elif ori == "right":
                ori = "up"
            elif ori == "down":
                ori = "right"
            else:
                ori = "down"
            x, y = forward(x, y, ori)
    return grid


def main():
    H, W, N = [int(i) for i in input().split()]
    grid = f(H, W, N)
    for i in grid:
        print("".join(i))

if __name__=="__main__":
    main()
