def Otoshidama(n, y):
  l = y//10000
  for i in range(l+1):
    m = n - i
    for j in range(m+1):
      s = n - i - j
      total = 10000*i + 5000*j + 1000*s
      if total == y:
        return [i, j, s]
  return [-1, -1, -1]

n, y = list(map(int, list(input().split())))
print(*Otoshidama(n, y))
