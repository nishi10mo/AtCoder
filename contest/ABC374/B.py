# Unvarnished Report
def f(S, T):
    if S == T:
        return 0
    ns = len(S)
    nt = len(T)
    n = min(ns, nt)
    for i in range(n):
        if S[i] != T[i]:
            return i + 1
    return n + 1

def main():
    S = list(input())
    T = list(input())
    print(f(S, T))

if __name__=="__main__":
    main()
