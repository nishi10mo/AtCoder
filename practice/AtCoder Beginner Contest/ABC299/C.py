# Dango
def f(N, S):
  def calc(N, S):
    ans = -1
    level = 0
    for i in range(N-1):
      if S[i]=="o" and S[i+1]=="o":
        level += 1
      elif S[i]=="o" and S[i+1]=="-":
        level += 1
        ans = max(level, ans)
        level = 0
    return ans
  ans1 = calc(N, S)
  S = S[::-1]
  ans2 = calc(N, S)
  return max(ans1, ans2)

def main():
  N = int(input())
  S = list(input())
  print(f(N, S))

if __name__=="__main__":
  main()
