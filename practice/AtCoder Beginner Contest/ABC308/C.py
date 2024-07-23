# Standings
def f(N, AB):
  results = []
  for i, ab in enumerate(AB):
    p = ab[0]*(10**100)//sum(ab)
    results.append([i+1, p])
  results = sorted(results, reverse=True, key=lambda x:x[1])
  ans = []
  for i in results:
    ans.append(i[0])
  return ans

def main():
  N = int(input())
  AB = []
  for _ in range(N):
    ab = [int(i) for i in input().split()]
    AB.append(ab)
  ans = f(N, AB)
  print(*ans)

if __name__=="__main__":
  main()

