# Exponential Plant
def calc(H):
  ans = 1
  s = 1
  while s <= H:
    s += 2**ans
    ans += 1
  return ans

def main():
  H = int(input())
  print(calc(H))

if __name__=="__main__":
  main()
