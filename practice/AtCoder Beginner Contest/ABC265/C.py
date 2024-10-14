# Belt Conveyor
def f(H, W, G):
    curr = [0, 0, ""]
    for _ in range(H*W):
        if G[curr[0]][curr[1]] == "U":
            curr[0] -= 1
            curr[2] = "U"
        elif G[curr[0]][curr[1]] == "D":
            curr[0] += 1
            curr[2] = "D"
        elif G[curr[0]][curr[1]] == "L":
            curr[1] -= 1
            curr[2] = "L"
        else:
            curr[1] += 1
            curr[2] = "R"
        if curr[0] < 0 or curr[0] > H-1 or curr[1] < 0 or curr[1] > W-1:
            if curr[2] == "U":
                curr[0] += 1
            elif curr[2] == "D":
                curr[0] -= 1
            elif curr[2] == "L":
                curr[1] += 1
            else:
                curr[1] -= 1     
            return curr[0]+1, curr[1]+1
    return -1

def main():
    H, W = [int(i) for i in input().split()]
    G = [[""]*W for _ in range(H)]
    for i in range(H):
        g = list(input())
        for j in range(W):
            G[i][j] = g[j]
    ans = f(H, W, G)
    if type(ans) == tuple:
        print(*ans)
    else:
        print(ans)
    
if __name__=="__main__":
    main()
