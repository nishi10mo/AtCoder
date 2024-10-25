# Monotonically Increasing
from itertools import permutations
def f(N, M):
    nums = [i+1 for i in range(M)]
    results = set()
    for perm in permutations(nums, N):
        perm = tuple(sorted(perm))
        results.add(perm)
    return results

def main():
    N, M = [int(i) for i in input().split()]
    results = f(N, M)
    for ans in results:
        print(*ans)

if __name__=="__main__":
    main()
