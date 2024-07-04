# 321-like Searcher
def f(K):
  ans = []
  for i in range(2, 1<<10):
    x = 0
    for j in range(9, -1, -1):
      if i & (1 << j):
        x *= 10
        x += j
    ans.append(x)

  ans = sorted(ans)
  return ans[K-1]

def main():
  K = int(input())
  print(f(K))

if __name__=="__main__":
  main()
