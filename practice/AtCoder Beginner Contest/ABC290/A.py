# Contest Result
def f(N, M, A, B):
    ans = 0
    for b in B:
        ans += A[b-1]
    return ans

def main():
    N, M = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    print(f(N, M, A, B))

if __name__ == '__main__':
    main()
