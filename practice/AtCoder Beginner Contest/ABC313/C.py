# Approximate Equalization 2
def f(N, A):
  A = sorted(A)
  total = sum(A)
  b = total//N
  b = [b]*N
  for i in range(total%N):
    b[N-1-i] += 1
  ans = 0
  for i in range(N):
    ans += abs(A[i]-b[i])
  return ans//2

def main():
  N = int(input())
  A = [int(i) for i in input().split()]
  print(f(N, A))

if __name__=="__main__":
  main()
