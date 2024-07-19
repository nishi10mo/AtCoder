# Reversible
def f(N, S):
  S_ = set()
  ans = 0
  for s in S:
    if s not in S_:
      S_.add(s)
      ans += 1
    s_rev = "".join(list(reversed(s)))
    S_.add(s_rev)
  return ans

def main():
  N = int(input())
  S = []
  for _ in range(N):
    s = input()
    S.append(s)
  print(f(N, S))

if __name__=="__main__":
  main()
