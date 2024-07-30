# Almost Equal
from itertools import permutations

def f(N, M, S):
    S = sorted(S)
    for s in permutations(S):
        ok = True
        for i in range(N-1):
            c = 0
            for j in range(M):
                if s[i][j] != s[i+1][j]:
                    c += 1
            if c > 1:
                ok = False
                break
        if ok:
            return "Yes"
    return "No"

def main():
    N, M = [int(i) for i in input().split()]
    S = []
    for _ in range(N):
        s = input()
        S.append(s)
    print(f(N, M, S))

if __name__=="__main__":
    main()
