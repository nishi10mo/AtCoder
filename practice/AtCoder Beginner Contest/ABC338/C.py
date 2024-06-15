# Leftover Recipes
def f(N, Q, A, B):
    INF = 10**18
    ans = 0
    for a in range(max(Q)+1):
        b = INF
        for i in range(N):
            if A[i]*a > Q[i]:
                b = -INF
            elif B[i] > 0:
                b = min(b, (Q[i]-A[i]*a)//B[i])
        ans = max(ans, a+b)
    return ans

def main():
    N = int(input())
    Q = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    print(f(N, Q, A, B))

if __name__=="__main__":
    main()
