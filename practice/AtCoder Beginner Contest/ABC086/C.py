import math

def Traveling(n, infos):
  for i in range(n):
    x = abs(infos[i][1] - infos[i+1][1])
    y = abs(infos[i][2] - infos[i+1][2])
    z = x + y
    t = infos[i+1][0] - infos[i][0]
    if (z > t) or (z%2==0 and t%2==1) or (z%2==1 and t%2==0):
      return "No"
  return "Yes"

n = int(input())
infos = [[0, 0, 0]]
for i in range(1, n+1):
  info = list(map(int, list(input().split())))
  infos.append(info)
print(Traveling(n, infos))

