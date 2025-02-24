# Simple path
import sys
sys.setrecursionlimit(10**6)
from collections import deque
def f(N, X, Y, graph):
    oya = [-1]*(N+1)
    oya[X] = 0
    deq = deque()
    deq.append(X)
    while deq:
        cur = deq.popleft()
        if cur == Y:
            break
        for nxt in graph[cur]:
            if oya[nxt] == -1:
                oya[nxt] = cur
                deq.append(nxt)
    ans = []
    cur = Y
    while cur:
        ans.append(cur)
        cur = oya[cur]
    return ans[::-1]

def main():
    N, X, Y = [int(i) for i in input().split()]
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v = [int(i) for i in input().split()]
        graph[u].append(v)
        graph[v].append(u)
    results = f(N, X, Y, graph)
    print(*results)

if __name__=="__main__":
    main()
