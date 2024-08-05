# PC on the Table
def f(H, W, S):
    i = 0
    while i < H:
        j = 0
        while j < W-1:
            if S[i][j]=="T" and S[i][j+1]=="T":
                S[i][j] = "P"
                S[i][j+1] = "C"
                j += 2
            else:
                j += 1
        i += 1
    return S

def main():
    H, W = [int(i) for i in input().split()]
    S = []
    for _ in range(H):
        s = list(input())
        S.append(s)
    S = f(H, W, S)
    for s in S:
        print("".join(s))

if __name__=="__main__":
    main()
