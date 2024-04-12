def KagamiMochi(n, d):
  d = list(set(d))
  d = sorted(d, reverse=True)
  return len(d)

n = int(input())
d = []
for i in range(n):
  d.append(int(input()))
print(KagamiMochi(n, d))
