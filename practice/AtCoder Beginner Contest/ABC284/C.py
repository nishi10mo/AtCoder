# Count Connected Components
from collections import deque
from collections import defaultdict
def f(N, M, graph):
    used = [False]*N
    que = deque()
    ans = 0
    for n in range(N):
        if used[n] == False:
            que.append(n)
            used[n] = True
            while que:
                q = que.popleft()
                for i in graph[q]:
                    if used[i] == False:
                        que.append(i)
                        used[i] = True
            ans += 1
    return ans

def main():
    N, M = [int(i) for i in input().split()]
    graph = defaultdict(list)
    for _ in range(M):
        p, q = [int(i)-1 for i in input().split()]
        graph[p].append(q)
        graph[q].append(p)
    print(f(N, M, graph))

if __name__=="__main__":
    main()
