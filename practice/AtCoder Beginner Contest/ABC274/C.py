# Ameba
def f(N, A):
    graph = dict(zip([i+1 for i in range(2*N+1)], [0]*(2*N+1)))
    for i in range(N):
        graph[2*(i+1)] = A[i]
        graph[2*(i+1)+1] = A[i]
    results = []
    for i in range(2*N+1):
        

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    print(f(N, A))

if __name__=="__main__":
    main()
