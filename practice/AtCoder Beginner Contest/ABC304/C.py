# Virus
from collections import deque 
def f(N, D, X, Y):
  graph = [[False]*N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      if ((X[i]-X[j])**2 + (Y[i]-Y[j])**2) <= D**2:
        graph[i][j] = True
  ans = [False]*N
  ans[0] = True
  que = deque()
  que.append(0)
  while que:
    i = que.popleft()
    for j in range(N):
      if graph[i][j] and not ans[j]:
        ans[j] = True
        que.append(j)
  results = []
  for i in ans:
    if i:
      results.append("Yes")
    else:
      results.append("No")
  return results

def main():
  N, D = [int(i) for i in input().split()]
  X = []
  Y = []
  for _ in range(N):
    x, y = [int(i) for i in input().split()]
    X.append(x)
    Y.append(y)
  results = f(N, D, X, Y)
  for i in results:
    print(i)

if __name__=="__main__":
  main()
