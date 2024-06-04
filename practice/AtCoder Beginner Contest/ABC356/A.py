# Subsegment Reverse
def calc(N, L, R):
  A = [i+1 for i in list(range(N))]
  left = A[:L-1]
  center = A[L-1:R]
  right = A[R:]
  center = sorted(center, reverse=True)
  A = left + center + right
  A = [str(i) for i in A]
  A = " ".join(A)
  return A

def main():
  N, L, R = [int(i) for i in input().split()]
  print(calc(N, L, R))

if __name__=="__main__":
  main()
