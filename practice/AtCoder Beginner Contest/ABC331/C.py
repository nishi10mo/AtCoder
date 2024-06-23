# Sum of Numbers Greater Than Me
from collections import defaultdict
def f(N, A):
  d = defaultdict(list)
  for i, a in enumerate(A):
    d[a].append(i)

  ans = [0]*N
  s = 0
  for v, i_list in sorted(d.items())[::-1]:
    for i in i_list:
      ans[i] = s
    s += v*len(i_list)
  return ans

def main():
  N = int(input())
  A = [int(i) for i in input().split()]
  ans = f(N, A)
  print(*ans)

if __name__=="__main__":
  main()
