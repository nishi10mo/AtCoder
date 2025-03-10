# Range Swap
def f(N, P, Q, R, S, A):
    return A[:P-1] + A[R-1:S] + A[Q:R-1] + A[P-1:Q] + A[S:]

def main():
    N, P, Q, R, S = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    print(*f(N, P, Q, R, S, A))

if __name__ == '__main__':
    main()
