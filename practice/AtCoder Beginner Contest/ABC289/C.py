#  Coverage
from itertools import combinations, chain
def f(N, M, C, S):
    ans = 0
    for i in range(1, M+1):
        for comb in combinations(S, i):
            comb = set(chain.from_iterable(comb))
            flag = True
            i = 1
            while flag and i<=N:
                if i in comb:
                    i += 1
                else:
                    flag = False
            if flag:
                ans += 1
    return ans

def main():
    N, M = [int(i) for i in input().split()]
    C = []
    S = []
    for _ in range(M):
        c = int(input())
        s = [int(i) for i in input().split()]
        C.append(c)
        S.append(s)
    print(f(N, M, C, S))

if __name__=="__main__":
    main()
