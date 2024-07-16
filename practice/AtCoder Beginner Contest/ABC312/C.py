# Invisible Hand
def f(N, M, A, B):
  A = sorted(A)
  B = sorted(B)
  sell = 0
  buy = M
  i = 0
  j = 0
  while i < N and j < M and sell < buy:
    if A[i] < B[j]+1:
      ans = A[i]
      sell += 1
      i += 1
    elif A[i] == B[j]+1:
      ans = A[i]
      sell += 1
      buy -= 1
      i += 1
      j += 1
    else:
      ans = B[j]+1
      buy -= 1
      j += 1
  if i == N:
    while j < M and sell < buy:
      ans = B[j]+1
      buy -= 1
      j += 1
  elif j == M:
    while i < N and sell < buy:
      ans = A[i]
      sell += 1
      i += 1
  return ans

def main():
  N, M = [int(i) for i in input().split()]
  A = [int(i) for i in input().split()]
  B = [int(i) for i in input().split()]
  print(f(N, M, A, B))

if __name__=="__main__":
  main()

