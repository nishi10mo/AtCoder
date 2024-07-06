# Slot Strategy 2 (Easy)
from itertools import permutations
def f(M, S):
  def solve(p, d):
    # tmp = []
    # for i in range(3):
    #   tmp.append(d not in S[i])
    # if any(tmp):
    #   return 10**9
    if any(d not in S[i] for i in range(3)): return 10**9
    crr = 0
    for i in range(3):
      crr += S[p[i]][crr%M:].index(d)+1
    return crr - 1

  ans = 10**9
  for d in range(10):
    P = permutations(range(3))
    for p in P:
      ans = min(ans, solve(p, d))
  if ans != 10**9:
    return ans
  else:
    return -1

def main():
  M = int(input())
  S = []
  for _ in range(3):
    s = [int(i) for i in list(input())]
    S.append(s+s)
  print(f(M, S))

if __name__=="__main__":
  main()
  
