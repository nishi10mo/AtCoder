# TaK Code
def f(N, M, S):
    ans = []
    for i in range(N-8):
        for j in range(M-8):
            flag = True
            for k in range(3):
                for l in range(3):
                    if S[i+k][j+l] != "#":
                        flag = False
                        break
                    if S[i+6+k][j+6+l] != "#":
                        flag = False
                        break
                if not flag:
                    break
            if not flag:
                continue
            for k in range(4):
                if S[i+k][j+3] != ".":
                    flag = False
                    break
                if S[i+3][j+k] != ".":
                    flag = False
                    break
                if S[i+5][j+5+k] != ".":
                    flag = False
                    break
                if S[i+5+k][j+5] != ".":
                    flag = False
                    break
            if not flag:
                continue
            ans.append([i+1, j+1])
    return ans

def main():
    N, M = [int(i) for i in input().split()]
    S = []
    for _ in range(N):
        s = list(input())
        S.append(s)
    results = f(N, M, S)
    for ans in results:
        print(*ans)

if __name__=="__main__":
    main()
