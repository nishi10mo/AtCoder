# Even Digits
def f(N):
  N -= 1
  ans = []
  while N:
    a = N % 5
    ans.append(a)
    N = N//5
  if not ans:
    ans.append(0)
  ans.reverse()
  ans = [i*2 for i in ans]
  return ans

def main():
  N = int(input())
  ans = f(N)
  ans = [str(i) for i in ans]
  print("".join(ans))

if __name__=="__main__":
  main()
