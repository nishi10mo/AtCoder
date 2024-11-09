# Sowing Stones
def f(N, M, X, A):
    if sum(A) < N:
        return -1
    ans = 0
    now = 0
    graph = [0]*N
    for i in range(M):
        graph[X[i]-1] += A[i]
    for i in range(N):
        if graph[i] != 0:
            continuex
        if i+1 < X[now]:
            return -1
        ans += i + 1 - X[now]
        A[now] -= 1
        if A[now] == 1:
            now += 1
    return ans

def main():
    N, M = [int(i) for i in input().split()]
    X = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    print(f(N, M, X, A))

if __name__=="__main__":
    main()
