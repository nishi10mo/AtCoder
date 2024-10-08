# Index × A(Continuous ver.)
def f(N, M, A):
    sumB_idx = []
    sumB_now = sum(A[:M])
    start = 0
    for i in range(M):
        start += (i+1)*A[i]
    sumB_idx.append(start)
    for i in range(N-M):
        next = sumB_idx[i] + M*A[i+M] - sumB_now
        sumB_idx.append(next)
        sumB_now = sumB_now - A[i] + A[i+M]
    return max(sumB_idx)

def main():
    N, M = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    print(f(N, M, A))

if __name__=="__main__":
    main()
