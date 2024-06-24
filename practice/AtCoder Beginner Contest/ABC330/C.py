# Minimize Abs 2
import math
def f(D):
  x = 0
  ans = 10**18
  while (x-1)**2 <= D:
    z = abs(D - x**2)
    y = math.isqrt(z)
    c1 = abs(x**2 + y**2 - D)
    c2 = abs(x**2 + (y+1)**2 - D)
    ans = min(ans, c1, c2)
    x += 1
  return ans

def main():
  D = int(input())
  print(f(D))

if __name__=="__main__":
  main()
