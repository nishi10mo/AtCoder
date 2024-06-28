# Peak
def f(N, M, A):
  A = sorted(A)
  A.append(10**18)
  ans = 0
  r = 0
  for l in range(N):
    while A[l] + M > A[r]:
      r += 1
    ans = max(ans, r-l)
  return ans

def main():
  N, M = [int(i) for i in input().split()]
  A = [int(i) for i in input().split()]
  print(f(N, M, A))

if __name__=="__main__":
  main()
