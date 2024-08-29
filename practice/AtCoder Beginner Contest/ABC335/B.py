# Tetrahedral Number
from itertools import permutations
def f(N):
    candidates = []
    for i in range(N+1):
        for x in range(i+1):
            if x > i-x:
                break
            for y in range(x, i+1):
                if y > i-x-y:
                    break
                z = i-x-y
                candidates.append([x, y, z])
    results = set()
    for xyz in candidates:
        for perm in permutations(xyz):
            results.add(perm)
    results = sorted(list(results))
    return results

def main():
    N = int(input())
    results = f(N)
    for ans in results:
        print(*ans)

if __name__=="__main__":
    main()

