# Counting Passes
def f(N, L, A):
    ans = 0
    for a in A:
        if a >= L:
            ans += 1
    return ans

def main():
    N, L = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    print(f(N, L, A))

if __name__=="__main__":
    main()
