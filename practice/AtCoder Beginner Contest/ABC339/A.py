# TLD
def f(S):
  ans = []
  for s in S:
    if s==".":
      ans = []
    else:
      ans.append(s)
  return ans

def main():
  S = list(input())
  ans = f(S)
  print("".join(ans))

if __name__=="__main__":
  main()
