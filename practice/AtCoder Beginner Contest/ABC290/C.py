# Max MEX
def f(N, K, A):
    ans = 0
    A = set(A)
    for i in range(K):
        if i in A:
            ans = i+1
        else:
            break
    return ans

def main():
    N, K = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    print(f(N, K, A))

if __name__=="__main__":
    main()
