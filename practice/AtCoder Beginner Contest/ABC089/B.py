def HinaArare(s):
  s = set(s)
  if len(s) == 3:
    return "Three"
  else:
    return "Four"

n = input()
s = list(input().split())
print(HinaArare(s))
