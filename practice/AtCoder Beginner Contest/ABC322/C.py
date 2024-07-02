# Festival
def f(N, M, A):
  m = 0
  results = []
  for n in range(1, N+1):
    ans = A[m] - n
    results.append(ans)
    if ans == 0:
      m += 1
  return results

def main():
  N, M = [int(i) for i in input().split()]
  A = [int(i) for i in input().split()]
  results = f(N, M, A)
  for ans in results:
    print(ans)

if __name__=="__main__":
  main()
