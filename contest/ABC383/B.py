# Humidifier 2
from itertools import combinations
def f(H, W, D, S):
    def count(comb0, comb1):
        c = 0
        for h in range(H):
            for w in range(W):
                if S[h][w] == ".":
                    if (abs(comb0[0] - h) + abs(comb0[1] - w)) <= D or (abs(comb1[0] - h) + abs(comb1[1] - w)) <= D:
                        c += 1
        return c
    cand = []
    for h in range(H):
        for w in range(W):
            if S[h][w] == ".":
                cand.append((h, w))
    ans = 0
    for comb in combinations(cand, 2):
        c = count(comb[0], comb[1])
        ans = max(ans, c)
    return ans

def main():
    H, W, D = [int(i) for i in input().split()]
    S = []
    for _ in range(H):
        s = list(input())
        S.append(s)
    print(f(H, W, D, S))

if __name__=="__main__":
    main()
