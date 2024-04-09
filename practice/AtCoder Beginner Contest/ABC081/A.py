def countOne(a, b, c):
  d = 0
  if(a == 1):
    d += 1
  if(b == 1):
    d += 1
  if(c == 1):
    d += 1
  return d

s1, s2, s3 = [int(i) for i in list(str(input()))]
print(countOne(s1, s2, s3))
