# Separated Lunch
from itertools import combinations
def f(N, K):
    total = sum(K)
    if total%2 == 0:
        half = total//2
    else:
        half = total//2 + 1
    cand = set()
    for i in range(N):
        for comb in combinations(K, i):
            comb_total = sum(comb)
            cand.add(comb_total)
    while True:
        if half in cand:
            return half
        half += 1

def main():
    N = int(input())
    K = [int(i) for i in input().split()]
    print(f(N, K))

if __name__=="__main__":
    main()
