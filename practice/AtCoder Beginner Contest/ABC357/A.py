# Sanitize Hands
def f(N, M ,H):
  ans = 0
  hand = 0
  for h in H:
    hand += h
    if hand <= M:
      ans += 1
    else:
      break
  return ans

def main():
  N, M = [int(i) for i in input().split()]
  H = [int(i) for i in input().split()]
  print(f(N, M, H))

if __name__=="__main__":
  main()
