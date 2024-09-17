# Circular Playlist
from itertools import accumulate
def f(N, T, A):
    total = sum(A)
    rem = T%total
    accumA = list(accumulate(A))
    ans = []
    if rem < A[0]:
        ans.append(1)
        ans.append(rem)
    for i in range(N-1):
        if accumA[i] < rem < accumA[i+1]:
            ans.append(i+2)
            ans.append(rem-accumA[i])
    return ans

def main():
    N, T = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    print(*f(N, T, A))

if __name__=="__main__":
    main()
