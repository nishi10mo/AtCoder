# Rotate and Palindrome
from collections import deque
def f(N, A, B, S):
    ans = 0
    for i in range(N//2):
        if S[i] != S[N-1-i]:
            ans += B
    for i in range(N-1):
        tmp = A*(i+1)
        que = deque(S)
        left = que.popleft()
        que.append(left)
        S = list(que)
        for i in range(N//2):
            if S[i] != S[N-1-i]:
                tmp += B
        ans = min(ans, tmp)
    return ans   

def main():
    N, A, B = [int(i) for i in input().split()]
    S = list(input())
    print(f(N, A, B, S))

if __name__=="__main__":
    main()
