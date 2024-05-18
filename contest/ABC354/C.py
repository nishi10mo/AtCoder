# AtCoder Magics
# def calc(N, A, C):
#   ans = [i+1 for i in range(N)]
#   minus = []
#   for i in range(N):
#     for j in range(N):
#       if A[i]>A[j] and C[i]<C[j]:
#         # ans.remove(j+1)
#         minus.append(j+1)
#   minus = set(minus)
#   for i in minus:
#     ans.remove(i)
#   return ans

def calc(N, A, C):
  A = sorted(A)
  ans = [i+1 for i in range(N)]
  minus = []
  for i in range(N):
    for j in range(i, N, 1):
      if C[i]>C[j]:
        # ans.remove(i+1)
        minus.append(i+1)
  minus = set(minus)
  for i in minus:
    ans.remove(i)
  return ans

def main():
  N = int(input())
  A = []
  C = []
  for i in range(N):
    A_, C_ = [int(i) for i in input().split()]
    A.append(A_)
    C.append(C_)
  ans = calc(N, A, C)
  print(len(ans))
  ans = [str(i) for i in ans]
  print(" ".join(ans))

if __name__=="__main__":
  main()
