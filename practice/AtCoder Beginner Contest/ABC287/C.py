# Path Graph?
from collections import deque
def f(N, M, graph):
    if N - M != 1:
        return "No"
    for i in graph:
        if len(i) > 2:
            return "No"
    que = deque()
    used = [False]*N
    que.append(0)
    while que:
        q = que.popleft()
        used[q] = True
        for i in graph[q]:
            if not used[i]:
                que.append(i)
    for i in used:
        if not i:
            return "No"
    return "Yes"

def main():
    N, M = [int(i) for i in input().split()]
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = [int(i)-1 for i in input().split()]
        graph[u].append(v)
        graph[v].append(u)
    print(f(N, M, graph))

if __name__=="__main__":
    main()
