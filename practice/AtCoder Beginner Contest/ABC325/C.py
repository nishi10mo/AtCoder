# Sensors
from collections import deque

def f(H, W, S):
  dx = [0, 0, 1, 1, 1, -1, -1, -1]
  dy = [1, -1, 1, 0, -1, 1, 0, -1]
  ans = 0
  used = [[False]*W for _ in range(H)]
  for i in range(H):
    for j in range(W):
      if S[i][j]=="." or used[i][j]:
        continue
      que = deque([(i, j)])
      while que:
        x, y = que.pop()
        for d in range(8):
          nx = x + dx[d]
          ny = y + dy[d]
          if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == "#" and not used[nx][ny]:
            used[nx][ny] = True
            que.append((nx, ny))
      ans += 1
  return ans

def main():
  H, W = [int(i) for i in input().split()]
  S = []
  for _ in range(H):
    s = list(input())
    S.append(s)
  print(f(H, W, S))

if __name__=="__main__":
  main()
