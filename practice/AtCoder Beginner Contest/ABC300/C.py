# Cross
from collections import deque
def f(H, W, C):
  N = min(H, W)
  ans = [0]*N
  used = [[False]*W for _ in range(H)]
  for i in range(H):
    for j in range(W):
      if C[i][j]=="#" and not used[i][j]:
        c = 1
        used[i][j] = True
        que = deque()
        que.append((i, j))
        while que:
          p, q = que.pop()
          if p < H-1 and q < W-1 and C[p+1][q+1]=="#" and not used[p+1][q+1]:
            que.append((p+1, q+1))
            used[p+1][q+1] = True
            c += 1
          if p < H-1 and q > 0 and C[p+1][q-1]=="#" and not used[p+1][q-1]:
            que.append((p+1, q-1))
            used[p+1][q-1] = True
            c += 1
          if p > 0 and q < W-1 and C[p-1][q+1]=="#" and not used[p-1][q+1]:
            que.append((p-1, q+1))
            used[p-1][q+1] = True
            c += 1
          if p > 0 and q > 0 and C[p-1][q-1]=="#" and not used[p-1][q-1]:
            que.append((p-1, q-1))
            used[p-1][q-1] = True
            c += 1
        size = (c-1)//4
        ans[size-1] += 1
  return ans

def main():
  H, W = [int(i) for i in input().split()]
  C = []
  for _ in range(H):
    c = list(input())
    C.append(c)
  print(*f(H, W, C))

if __name__=="__main__":
  main()
  