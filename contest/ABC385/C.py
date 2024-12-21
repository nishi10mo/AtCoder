# Illuminate Buildings
from collections import defaultdict
from itertools import combinations
def f(N, H):
    num = defaultdict(list)
    for i in range(N):
        num[H[i]].append(i)
    ans = 0
    candidates = []
    for i, v in num.items():
        if len(v) == 1 or len(v) == 2:
            ans = max(ans, len(v))
        elif len(v) >= 3:
            candidates.append(v)
    for candidate in candidates:
        for c in range(3, len(candidate)+1):
            for comb in combinations(candidate, c):
                diff = comb[1] - comb[0]
                flag = True
                for i in range(1, len(comb)-1):
                    if comb[i+1] - comb[i] != diff:
                        flag = False
                        break
                if flag:
                    ans = max(ans, len(comb))
    return ans

def main():
    N = int(input())
    H = [int(i) for i in input().split()]
    print(f(N, H))

if __name__ == '__main__':
    main()
