# racecar
from itertools import permutations
def f(N, S):
    for perm in permutations(S, 2):
        forward = perm[0] + perm[1]
        backward = "".join([i for i in reversed(forward)])
        if forward == backward:
            return "Yes"
    return "No"

def main():
    N = int(input())
    S = []
    for _ in range(N):
        s = input()
        S.append(s)
    print(f(N, S))

if __name__=="__main__":
    main()
