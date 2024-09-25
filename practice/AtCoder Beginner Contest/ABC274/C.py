# Ameba
def f(N, A):
    graph = dict(zip([i+1 for i in range(2*N+1)], [0]*(2*N+1)))
    for i in range(N):
        graph[2*(i+1)] = A[i]
        graph[2*(i+1)+1] = A[i]
    results = [0]
    for i in range(1, 2*N+1):
        parents = graph[i+1]
        c = results[parents-1] + 1
        results.append(c)
    return results

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    results = f(N, A)
    for ans in results:
        print(ans)

if __name__=="__main__":
    main()
