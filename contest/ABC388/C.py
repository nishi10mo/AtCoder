# Various Kagamimochi
def f(N, A):
    ans = 0
    l = 0
    r = 0
    while l < N:
        if A[l]*2 <= A[r]:
            ans += N - r
            l += 1
        else:
            if r < N-1:
                r += 1
            else:
                break
    return ans

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    print(f(N, A))

if __name__ == '__main__':
    main()
