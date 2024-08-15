# Don’t be cycle
from collections import deque
def f(N, M, graph):
    s = 0
    used = [False]*N
    for i in range(N):
        if not used[i]:
            s += 1
            que = deque()
            que.append(i)
            used[i] = True
            while que:
                q = que.pop()
                used[q] = True
                for v in graph[q]:
                    if not used[v]:
                        used[v] = True
                        que.append(v)
    return M - N + s

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
