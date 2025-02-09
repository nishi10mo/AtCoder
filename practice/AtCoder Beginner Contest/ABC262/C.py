# Min Max Pair
from itertools import combinations
def f(N, a):
    same_num = 0
    reverse_num = 0
    for i in range(N):
        if i+1 == a[i]:
            same_num += 1
        elif a[a[i]-1] == i+1:
            reverse_num += 1
    return same_num*(same_num-1)//2 + reverse_num//2

def main():
    N = int(input())
    a = [int(i) for i in input().split()]
    print(f(N, a))

if __name__ == '__main__':
    main()
