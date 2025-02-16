# Qualification Contest
def f(N, K, S):
    results = sorted(S[:K])
    return results

def main():
    N, K = [int(i) for i in input().split()]
    S = []
    for _ in range(N):
        S.append(input())
    results = f(N, K, S)
    for ans in results:
        print(ans)

if __name__ == '__main__':
    main()
