# Previous Permutation
from itertools import permutations
def f(N, P):
    i = N - 2
    while P[i] < P[i+1]:
        i -= 1
    j = N - 1
    while P[j] > P[i]:
        j -= 1
    P[i], P[j] = P[j], P[i]
    return P[:i+1] + P[:i:-1]

def main():
    N = int(input())
    P = [int(i) for i in input().split()]
    print(*f(N, P))

if __name__=="__main__":
    main()
