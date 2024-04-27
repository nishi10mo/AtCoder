def SpotTheDifference(n, a, b):
  for i in range(n):
    for j in range(n):
      if a[i][j] != b[i][j]:
        ans = str(i+1)+" "+str(j+1)
        return ans

n = int(input())
a = []
b = []
for i in range(n):
  a_ = list(input())
  a.append(a_)
for i in range(n):
  b_ = list(input())
  b.append(b_)
print(SpotTheDifference(n, a, b))
