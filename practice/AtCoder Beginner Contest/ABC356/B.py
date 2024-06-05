# Nutrients
import numpy as np
def calc(N, M, A, X):
  X = np.array(X)
  sumCol = np.sum(X, axis=0)
  sumCol = sumCol.tolist()
  for i in range(M):
    if A[i] > sumCol[i]:
      return "No"
  return "Yes"

def main():
  N, M = [int(i) for i in input().split()]
  A = [int(i) for i in input().split()]
  X = []
  for _ in range(N):
    x = [int(i) for i in input().split()]
    X.append(x)
  print(calc(N, M, A, X))

if __name__=="__main__":
  main()
