# Print 341
def f(N):
  ans = []
  for i in range(2*N+1):
    if i%2==0:
      ans.append(1)
    else:
      ans.append(0)
  return ans

def main():
  N = int(input())
  ans = f(N)
  ans = [str(i) for i in ans]
  print("".join(ans))

if __name__=="__main__":
  main()
