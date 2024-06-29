# Adjacency Matrix
def f(N, A):
  ans = []
  for a in A:
    tmp = []
    for i, val in enumerate(a):
      if val == 1:
        tmp.append(i+1)
    ans.append(tmp)
  return ans

def main():
  N = int(input())
  A = []
  for _ in range(N):
    a = [int(i) for i in input().split()]
    A.append(a)
  ans = f(N, A)
  for i in ans:
    print(*i)

if __name__=="__main__":
  main()
  