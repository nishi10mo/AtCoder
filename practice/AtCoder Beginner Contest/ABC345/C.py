# One Time Swap
def calc(S):
  n = len(S)
  S_ = list(set(S))
  ans = n*(n-1)//2
  flag = False
  for i in S_:
    c = S.count(i)
    if c > 1:
      minus = c*(c-1)//2
      ans -= minus
      flag = True
  if flag == True:
    ans += 1
  return ans

def main():
  S = list(input())
  print(calc(S))

if __name__=="__main__":
  main()
