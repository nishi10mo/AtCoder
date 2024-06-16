# Lining Up 2
def f(N, A):
  dic = {}
  for i in range(N):
    dic[A[i]] = i+1
  ans = []
  nx = -1
  tmp = dic[nx]
  ans.append(tmp)
  for _ in range(N-1):
    tmp = dic[tmp]
    ans.append(tmp)
  return ans

def main():
  N = int(input())
  A = [int(i) for i in input().split()]
  ans = f(N, A)
  ans = [str(i) for i in ans]
  print(" ".join(ans))

if __name__=="__main__":
  main()
