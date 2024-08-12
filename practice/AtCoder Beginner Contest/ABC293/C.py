# Make Takahashi Happy
from collections import deque

def f(H, W, A):
    ans = 0
    que = deque()
    que.append((0, 0))
    his = {}
    while que:
        h, w = que.pop()
        if A[h][w] in his:
            continue
        else:
            his.add(A[h][w])
        if h==H-1 and w==W-1:
            ans += 1
            his = {}
        elif h<H-1 and w<W-1:
            que.append((h+1, w))
            que.append((h, w+1))
        elif h<H-1 and w==W-1:
            que.append((h+1, w))
        elif h==H-1 and w<W-1:
            que.append((h, w+1))
        



def main():
    H, W = [int(i) for i in input().split()]
    A = []
    for _ in range(H):
        a = [int(i) for i in input().split()]
        A.append(a)