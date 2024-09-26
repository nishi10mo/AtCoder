# (K+1)-th Largest Number
from collections import defaultdict

def f(N, A):
    A_set = set(A)
    A_set = sorted(list(A_set))
    A_counts = defaultdict(int)
    A_kind = defaultdict(int)
    for a in A:
        A_counts[a] += 1
    for i in range(len(A_set)):
        A_kind[len(A_set) - i - 1] = A_set[i]
    results = []
    for i in range(N):
        kind = A_kind[i]
        ans = A_counts[kind]
        results.append(ans)
    return results

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    results = f(N, A)
    for ans in results:
        print(ans)

if __name__=="__main__":
    main()

