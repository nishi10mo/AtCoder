# Prefix and Suffix
def f(N, M, S, T):
    cand = [0, 1, 2, 3]
    for i in range(N):
        if S[i] != T[i]:
            cand = [2, 3]
    for i in range(1, N+1):
        if S[-i] != T[-i]:
            if cand == [2, 3]:
                return 3
            if cand == [0, 1, 2, 3]:
                return 1
    if cand == [2, 3]:
        return 2
    else:
        return 0

def main():
    N, M = [int(i) for i in input().split()]
    S = list(input())
    T = list(input())
    print(f(N, M, S, T))

if __name__=="__main__":
    main()
