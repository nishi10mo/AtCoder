# Ladder Takahashi
from collections import defaultdict, deque
def f(N, graph):
    ans = 1
    que = deque()
    que.append(1)
    used = defaultdict(lambda: False)
    used[1] = True
    while que:
        q = que.popleft()
        ans = max(ans, q)
        for i in graph[q]:
            if not used[i]:
                que.append(i)
                used[i] = True
    return ans

def main():
    N = int(input())
    graph = defaultdict(list)
    for _ in range(N):
        a, b = [int(i) for i in input().split()]
        graph[a].append(b)
        graph[b].append(a)
    print(f(N, graph))

if __name__=="__main__":
    main()
    
