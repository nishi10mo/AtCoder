# Simple path
# 以下のコードはTRE, MRE
import sys
sys.setrecursionlimit(10**6)

from collections import defaultdict, deque
def f(N, X, Y, graph):
    used = defaultdict(lambda: False)
    deq = deque()
    stop = False
    def dfs(start, end):
        nonlocal stop
        if not stop:
            deq.append(start)
        if start == end:
            stop = True
        used[start] = True
        for neighbor in graph[start]:
            if not used[neighbor]:
                dfs(neighbor, end)
                if stop:
                    return
        if not stop:
            deq.pop()
    dfs(X, Y)
    return deq

def main():
    N, X, Y = [int(i) for i in input().split()]
    graph = defaultdict(list)
    for _ in range(N-1):
        u, v = [int(i) for i in input().split()]
        graph[u].append(v)
        graph[v].append(u)
    ans = f(N, X, Y, graph)
    print(*ans)

if __name__=="__main__":
    main()
