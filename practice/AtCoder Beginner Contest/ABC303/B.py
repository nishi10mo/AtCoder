# Discord
def f(N, M, A):
    graph = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                graph[i][j] = True
    for a in A:
        for i in range(N-1):
            graph[a[i]-1][a[i+1]-1] = True
            graph[a[i+1]-1][a[i]-1] = True
    ans = sum(row.count(False) for row in graph)
    ans = ans//2
    return ans

def main():
    N, M = [int(i) for i in input().split()]
    A = []
    for _ in range(M):
        a = [int(i) for i in input().split()]
        A.append(a)
    print(f(N, M, A))

if __name__=="__main__":
    main()
    
