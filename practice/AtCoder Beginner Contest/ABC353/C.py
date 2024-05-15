# Sigma Problem
def calc(N, A):
    A.sort()
    r = N
    cnt = 0
    ans = 0
    for i in range(N):
        r = max(r, i+1)
        while r-1 > i and A[r-1] + A[i] >= 10**8:
            r -= 1
        cnt += N-r
    for i in range(N):
        ans += A[i]*(N-1)
    ans -= cnt*(10**8)
    return ans

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    print(calc(N, A))

if __name__=="__main__":
    main()
