# 1 2 1 3 1 2 1 
from functools import cache
@cache
def f(N):
  return "1" if N==1 else f(N-1) + " " + str(N) + " " + f(N-1) 

def main():
  N = int(input())
  print(f(N))

if __name__=="__main__":
  main()
