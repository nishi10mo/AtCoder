# Base 2
def f(A):
    n = len(A)
    ans = 0
    for i in range(n):
        ans += A[i]*(2**i)
    return ans

def main():
    A = [int(i) for i in input().split()]
    print(f(A))

if __name__=="__main__":
    main()
