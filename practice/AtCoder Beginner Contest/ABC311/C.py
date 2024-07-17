# Find it!
def f(N, A):
  for i in range(N):
    result = []
    start = A[i]
    tmp = A[i]
    result.append(tmp)
    for _ in range(N):
      tmp = A[tmp-1]
      if start == tmp:
        break
      result.append(tmp)
  return result      

def main():
  N = int(input())
  A = [int(i) for i in input().split()]
  result = f(N, A)
  print(len(result))
  print(*result)

if __name__=="__main__":
  main()
