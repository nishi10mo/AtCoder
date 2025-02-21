# Postal Card
def f(N, M, S, T):
    ans = 0
    for s in S:
        for t in T:
            if s[3:] == t:
                ans += 1
    return ans

def main():
    N, M = [int(i) for i in input().split()]
    S = []
    for _ in range(N):
        S.append(input())
    T = set()
    for _ in range(M):
        T.add(input())
    print(f(N, M, S, T))

if __name__ == '__main__':
    main()
