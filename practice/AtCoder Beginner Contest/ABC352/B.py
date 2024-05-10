# Typing 
def pTrueStr(S, T):
  c = 0
  ans = []
  for i in range(len(T)):
    if T[i] == S[c]:
      ans.append(i+1)
      c += 1
  return ans

def main():
  S = list(input())
  T = list(input())
  ans = pTrueStr(S, T)
  ans = [str(i) for i in ans]
  print(" ".join(ans))
  
if __name__=="__main__":
  main()
