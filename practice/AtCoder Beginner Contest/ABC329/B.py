# Next
def f(N, A):
    A = set(A)
    maxA = max(A)
    ans = 0
    for a in A:
        if a != maxA:
            ans = max(ans, a)
    return ans

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    print(f(N, A))

if __name__=="__main__":
    main()
