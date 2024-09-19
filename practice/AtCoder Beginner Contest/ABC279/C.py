# RANDOM
import numpy as np
def f(H, W, S, T):
    S_cols = [[] for _ in range(W)]
    T_cols = [[] for _ in range(W)]
    for s in S:
        for i in range(W):
            S_cols[i].append(s[i])
    for t in T:
        for i in range(W):
            T_cols[i].append(t[i])
    S_cols = sorted(S_cols)
    T_cols = sorted(T_cols)
    if S_cols == T_cols:
        return "Yes"
    else:
        return "No"

def main():
    H, W = [int(i) for i in input().split()]
    S = []
    T = []
    for _ in range(H):
        s = list(input())
        S.append(s)
    for _ in range(H):
        t = list(input())
        T.append(t)
    print(f(H, W, S, T))

if __name__=="__main__":
    main()
