# Consecutive
def f(N, Q, S, LR):
  A = [0]*N
  B = [0]*N
  for i in range(N-1):
    if S[i] == S[i+1]:
      A[i] += 1
  for i in range(1, N):
    B[i] = B[i-1] + A[i-1]
  ans = []
  for lr in LR:
    l, r = lr
    tmp = B[r-1] - B[l-1]
    ans.append(tmp)
  return ans

def main():
  N, Q = [int(i) for i in input().split()]
  S = list(input())
  LR = []
  for _ in range(Q):
    lr = [int(i) for i in input().split()]
    LR.append(lr)
  ans = f(N, Q, S, LR)
  for i in ans:
    print(i)

if __name__=="__main__":
  main()
  