# Vertical Writing
def f(N, S, m):
    for s in S:
        while len(s) < m:
            s.append("*")
    T = [[] for _ in range(m)]
    for j in range(m):
        for i in range(N-1, -1, -1):
            T[j].append(S[i][j])
    for t in T:
        while t[-1]=="*":
            t.pop()
    return T

def main():
    N = int(input())
    S = []
    m = 0
    for _ in range(N):
        s = list(input())
        m = max(m, len(s))
        S.append(s)
    T = f(N, S, m)
    for t in T:
        print("".join(t))

if __name__=="__main__":
    main()
