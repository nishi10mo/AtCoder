# AtCoder Amusement Park
def calc(N, K, A):
  train = []
  ans = 0
  i = 0
  while i < N:
    train.append(A[i])
    if sum(train) > K:
      train = []
      ans += 1
      i -= 1
    i += 1
  ans += 1
  return ans

def main():
  N, K = [int(i) for i in input().split()]
  A = [int(i) for i in input().split()]
  print(calc(N, K, A))

if __name__=="__main__":
  main()
