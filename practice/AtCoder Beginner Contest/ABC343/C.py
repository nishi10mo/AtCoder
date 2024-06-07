# 343
import math
def calc(N):
  ans = 1
  i = 1
  while i**3 <= N:
    tmp = i**3
    if str(tmp) == str(tmp)[::-1]:
      ans = tmp
    i += 1
  return ans

def main():
  N = int(input())
  print(calc(N))

if __name__=="__main__":
  main()
