# Which is ahead?
def f(N, P, Q, AB):
  ordr = {}
  for i, val in enumerate(P):
    ordr[val] = i+1
  ans = []
  for ab in AB:
    q1 = ordr[ab[0]]
    q2 = ordr[ab[1]]
    if q1 < q2:
      ans.append(ab[0])
    else:
      ans.append(ab[1])
  return ans

def main():
  N = int(input())
  P = [int(i) for i in input().split()]
  Q = int(input())
  AB = []
  for _ in range(Q):
    ab = [int(i) for i in input().split()]
    AB.append(ab)
  results = f(N, P, Q, AB)
  for ans in results:
    print(ans)

if __name__=="__main__":
  main()
  