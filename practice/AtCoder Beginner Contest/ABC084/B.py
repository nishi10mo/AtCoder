def PostalCode(a, b, s):
  for i in range(a):
    if s[i] == "-":
      return "No"
  if s[a] != "-":
    return "No"
  for i in range(a+1, a+b+1):
    if s[i] == "-":
      return "No"
  return "Yes"

a, b = list(map(int, list(input().split())))
s = list(input())
print(PostalCode(a, b, s))
