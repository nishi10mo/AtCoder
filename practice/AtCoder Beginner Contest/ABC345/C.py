# One Time Swap
def calc(S):
  n = len(S)
  if n == 1:
    return 1
  S_ = list(set(S))
  ans = n*(n-1)//2
  for i in S_:
    c = S.count(i)
    if c > 1:
      minus = c*(c-1)//2 - 1
      ans -= minus
  return ans

def main():
  S = list(input())
  print(calc(S))

if __name__=="__main__":
  main()
