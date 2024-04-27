def MergeTheBalls(n, a):
  b = []
  for i in range(n):
    b.append(a[i])
    while True:
      if len(b)<=1:
        break
      if b[-2]!=b[-1]:
        break
      else:
        for i in range(2):
          c = b.pop()
        b.append(c+1)
  return len(b)

n = int(input())
a = list(map(int, list(input().split())))
print(MergeTheBalls(n, a))
