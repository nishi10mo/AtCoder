# Invisible Hand
def f(N, M, A, B):
  A = sorted(A)
  B = sorted(B)
  sell = 0
  buy = M
  i = 0
  j = 0
  while sell < buy:
    if A[i] < B[j]+1:
      ans = A[i]
      sell += 1
      if i < N-1:
        i += 1
    elif A[i] == B[j]+1:
      ans = A[i]
      sell += 1
      buy -= 1
      if i < N-1:
        i += 1
      if j < M-1:
        j += 1
    else:
      ans = B[j]+1
      buy -= 1
      if j < M-1:
        j += 1
    print("i", i)
    print("j", j)
    print("sell", sell)
    print("buy", buy)
    print("ans", ans)
  return ans

def main():
  N, M = [int(i) for i in input().split()]
  A = [int(i) for i in input().split()]
  B = [int(i) for i in input().split()]
  print(f(N, M, A, B))

if __name__=="__main__":
  main()

# 反例
1 3
100
200 150 300
