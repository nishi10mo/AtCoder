# Zero Sum Game
def main():
  n = int(input())
  A = list(map(int, list(input().split())))
  ans = 0 - sum(A)
  print(ans)

if __name__=="__main__":
  main()
