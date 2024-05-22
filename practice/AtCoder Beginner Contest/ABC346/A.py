# Adjacent Product
def calc(N, A):
  ans = []
  for i in range(N-1):
    tmp = A[i]*A[i+1]
    ans.append(tmp)
  return ans

def main():
  N = int(input())
  A = [int(i) for i in input().split()]
  ans = calc(N, A)
  ans = [str(i) for i in ans]
  print(" ".join(ans))

if __name__=="__main__":
  main()

