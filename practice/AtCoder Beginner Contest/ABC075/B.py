def Minesweeper(h, w, s):
  def checkBom(i, j, h, w, s):
    bom = 0
    if i > 0 and j > 0 and s[i-1][j-1]=="#":
      bom += 1
    if i > 0 and s[i-1][j]=="#":
      bom += 1
    if i > 0 and j < w-1 and s[i-1][j+1]=="#":
      bom += 1
    if j > 0 and s[i][j-1]=="#":
      bom += 1
    if j < w-1 and s[i][j+1]=="#":
      bom += 1
    if i < h-1 and j > 0 and s[i+1][j-1]=="#":
      bom += 1
    if i < h-1 and s[i+1][j]=="#":
      bom += 1
    if i < h-1 and j < w-1 and s[i+1][j+1]=="#":
      bom += 1
    return str(bom)

  for i in range(h):
    for j in range(w):
      if s[i][j] == "#":
        continue
      s[i][j] = checkBom(i, j, h, w, s)
  return s

h, w = list(map(int, list(input().split())))
s = []
for i in range(h):
  s_ = list(input())
  s.append(s_)
s = Minesweeper(h, w, s)
for i in range(h):
  print("".join(s[i]))
