# Medicine
def f(N, K, AB):
  AB = sorted(AB, key=lambda x:x[0])
  total = [sum(i) for i in zip(*AB)][1]
  if total <= K:
    return 1
  for i in range(N):
    total -= AB[i][1]
    if total <= K:
      return AB[i][0]+1

def main():
  N, K = [int(i) for i in input().split()]
  AB = []
  for _ in range(N):
    ab = [int(i) for i in input().split()]
    AB.append(ab)
  print(f(N, K, AB))

if __name__=="__main__":
  main()
