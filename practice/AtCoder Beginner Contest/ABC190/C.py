from collections import Counter

def BowlsAndDishes(bit, k, cond, choices):
  counter = Counter()
  for i in range(k):
    choice = choices[i][bit >> i & 1]
    counter[choice] += 1
  
  ret = 0
  for a, b in cond:
    if counter[a]>0 and counter[b]>0:
      ret += 1
  return ret

n, m = map(int, input().split())
cond = []
for _ in range(m):
  a, b = map(int, input().split())
  cond.append([a, b])
k = int(input())
choices = []
for _ in range(k):
  c, d = map(int, input().split())
  choices.append([c, d])

ans = 0
for bit in range(1 << k):
  ans = max(ans, BowlsAndDishes(bit, k, cond, choices))
print(ans)


