# Keys
# 関数呼び出しのオーバーヘッドや変数アクセスの違いによりTLEに
def calc(N, M, K, C, A, R):
  ans = 0
  for bit in range(1 << N):
    judge = True
    for i in range(M):
      cnt = 0
      for j in A[i]:
        if bit>>j&1:
          cnt += 1
      if (cnt >= K and R[i] == "o") or (cnt < K and R[i] =="x"):
        continue
      else:
        judge = False
        break
    if judge:
      ans += 1
  return ans

def main():
  N, M, K = [int(i) for i in input().split()]
  C = []
  A = []
  R = []
  for _ in range(M):
    c, *a, r = input().split()
    c = int(c)
    a = [int(i)-1 for i in a]
    C.append(c)
    A.append(a)
    R.append(r)
  print(calc(N, M, K, C, A, R))

if __name__=="__main__":
  main()
