# Divisible
def calc(N, K, A):
    ans = []
    for i in range(N):
        if A[i]%K==0:
            tmp = A[i]//K
            ans.append(tmp)
    return ans

def main():
    N, K = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    ans = calc(N, K, A)
    ans = [str(i) for i in ans]
    print(" ".join(ans))

if __name__=="__main__":
    main()

