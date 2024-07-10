# Flavors
def f(N, FS):
  def diff(i):
    nonlocal N
    j = i+1
    while j <= N-1:
      if FS[i][0] != FS[j][0]:
        return FS[i][1] + FS[j][1]
      else:
        j += 1
    return 0
  
  def same(i):
    nonlocal N
    j = i+1
    while j <= N-1:
      if FS[i][0] == FS[j][0]:
        return FS[i][1] + FS[j][1]//2
      else:
        j += 1
    return 0

  FS = sorted(FS, reverse=True, key=lambda x:x[1])
  ans1 = diff(0)
  ans2 = same(0)
  ans3 = diff(1)
  ans = max(ans1, ans2, ans3)
  return ans

def main():
  N = int(input())
  FS = []
  for _ in range(N):
    fs = [int(i) for i in input().split()]
    FS.append(fs)
  print(f(N, FS))

if __name__=="__main__":
  main()
