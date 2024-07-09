# Remembering the Days
def f(N, M, E):
  ans = 0
  used = [False]*(N+1)
  def dfs(v, s):
    nonlocal ans
    used[v]=True
    if s > ans:
      ans = s
    for i in range(1, N+1):
      if not used[i] and E[v][i]:
        dfs(i, s+E[v][i])
    used[v] = False
  for i in range(1, N+1):
    dfs(i, 0)
  return ans

def main():
  N, M = [int(i) for i in input().split()]
  E = [[0]*(N+1) for _ in range(N+1)]
  for _ in range(M):
    a, b, c = [int(i) for i in input().split()]
    E[a][b] = c
    E[b][a] = c
  print(f(N, M, E))

if __name__=="__main__":
  main()
  