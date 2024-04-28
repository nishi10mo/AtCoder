def ManyFormulas(s):
  ans = 0
  n = len(s)
  for i in range(1 << (n-1)):
    sm = 0
    a = s[0]
    for j in range(n-1):
      if i & (1 << j):
        sm += a
        a = 0
      a = 10*a + s[j+1]
    sm += a
    ans += sm
  return ans

s = list(map(int, list(input())))
print(ManyFormulas(s))
