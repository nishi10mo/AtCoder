# Roulette
def f(N, C, A, X):
    minc = 40
    ans = []
    for i in range(N):
        for j in range(C[i]):
            if A[i][j] == X:
                if C[i] < minc:
                    minc = C[i]
                    ans = [i+1]
                elif C[i] == minc:
                    ans.append(i+1)
    return ans

def main():
    N = int(input())
    C = []
    A = []
    for _ in range(N):
        c = int(input())
        a = [int(i) for i in input().split()]
        C.append(c)
        A.append(a)
    X = int(input())
    ans = f(N, C, A, X)
    print(len(ans))
    print(*ans)

if __name__=="__main__":
    main()
