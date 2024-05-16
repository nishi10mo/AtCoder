# Penalty Kick
def calc(N):
  ans = []
  for i in range(N):
    if i%3==2:
      ans.append("x")
    else:
      ans.append("o")
  ans = "".join(ans)
  return ans

def main():
  N = int(input())
  print(calc(N))

if __name__=="__main__":
  main()
