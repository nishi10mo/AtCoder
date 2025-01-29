# Many A+B Problems
def f(N, A, B):
    results = []
    for i in range(N):
        results.append(A[i] + B[i])
    return results

def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = [int(i) for i in input().split()]
        A.append(a)
        B.append(b)
    results = f(N, A, B)
    for ans in results:
        print(ans)

if __name__ == '__main__':
    main()
