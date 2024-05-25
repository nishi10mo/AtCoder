# Piano 2
def calc(N, M, A, B):
  A = sorted(A)
  B = sorted(B)
  i = 0
  j = 0
  flag = 0
  while i < N-1:
    if A[i] <= B[j]:
      i += 1
      flag += 1
      if flag == 2:
        return "Yes"
    else:
      if j == M-1:
        return "Yes"
      j += 1
      flag = 0
  return "No"

def main():
  N, M = [int(i) for i in input().split()]
  A = [int(i) for i in input().split()]
  B = [int(i) for i in input().split()]
  print(calc(N, M, A, B))

if __name__=="__main__":
  main()
