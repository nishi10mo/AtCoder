# T-shirts
def f(N, M, S):
  ans = 0
  tmp = 0
  m = M
  for i in S:
    if i == 0:
      ans = max(ans, tmp)
      tmp = 0
      m = M
    elif i == 1:
      if m == 0:
        tmp += 1
      else:
        m -=1
    else:
      tmp += 1
  ans = max(ans, tmp)
  return ans

def main():
  N, M = [int(i) for i in input().split()]
  S = list(input())
  S = [int(i) for i in S]
  print(f(N, M, S))

if __name__=="__main__":
  main()
