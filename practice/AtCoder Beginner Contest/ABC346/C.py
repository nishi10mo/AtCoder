# Σ
# def calc(N, K, A):
#   klist = set(range(1, K+1))
#   A = set(A)
#   ans = list(klist - A)
#   ans = sum(ans)
#   return ans

def calc(N, K, A):
  ans = (1+K)*K//2
  A = set(A)
  for i in A:
    if i <= K:
      ans -= i
  return ans

def main():
  N, K = [int(i) for i in input().split()]
  A = [int(i) for i in input().split()]
  print(calc(N, K, A))

if __name__=="__main__":
  main()
