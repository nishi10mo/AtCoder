# Default Price
from collections import defaultdict

def f(N, M, C, D, P):
    graph = defaultdict(lambda: P[0])
    for i in range(M):
        graph[D[i]] = P[i+1]
    ans = 0
    for c in C:
        ans += graph[c]
    return ans

def main():
    N, M = [int(i) for i in input().split()]
    C = list(input().split())
    D = list(input().split())
    P = [int(i) for i in input().split()]
    print(f(N, M, C, D, P))

if __name__=="__main__":
    main()
