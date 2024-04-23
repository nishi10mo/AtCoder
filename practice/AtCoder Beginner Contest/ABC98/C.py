def Attention(n, s):
  pre = s.count("E")
  cur = pre
  for i in range(n):
    if pre < cur:
      cur = pre
    if s[i]=="W":
      pre += 1
    if s[i]=="E":
      pre -= 1
  if pre <= cur:
    return pre
  else:
    return cur

n = int(input())
s = list(input())
print(Attention(n, s))
