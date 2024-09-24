# Previous Permutation
from itertools import permutations
def f(N, P):
    p = [i+1 for i in range(N)]
    for perm in permutations(p):
        if perm == P:
            return before
        before = perm

def main():
    N = int(input())
    P = tuple([int(i) for i in input().split()])
    print(*f(N, P))

if __name__=="__main__":
    main()
