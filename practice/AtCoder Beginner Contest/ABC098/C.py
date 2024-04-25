# def Attention(n, s):
#   pre = s.count("E")
#   cur = pre
#   for i in range(n):
#     if pre < cur:
#       cur = pre
#     if s[i]=="W":
#       pre += 1
#     if s[i]=="E":
#       pre -= 1
#   if pre <= cur:
#     return pre
#   else:
#     return cur

def Attention(n, s):
  tmp = s.count("E")
  ans = tmp
  for i in range(n):
    if s[i]=="W":
      tmp += 1
    if s[i]=="E":
      tmp -= 1
    if tmp < ans:
      ans = tmp
  return ans

n = int(input())
s = list(input())
print(Attention(n, s))
