# Socks
from collections import defaultdict
def f(N: int, A: list) ->int:
    socks = defaultdict(int)
    for a in A:
        socks[a] += 1
    ans = 0
    for val in socks.values():
        ans += val//2
    return ans

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    print(f(N, A))

if __name__=="__main__":
    main()
