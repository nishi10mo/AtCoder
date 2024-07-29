# Dash
def f(N, M, H, K, S, XY):
  x = 0
  y = 0
  h = H
  for i in range(N):
    if S[i]=="L":
      x -= 1
    elif S[i]=="R":
      x += 1
    elif S[i]=="U":
      y += 1
    elif S[i]=="D":
      y -= 1
    h -= 1
    if h < 0:
      return "No"
    if h < K and ((x, y) in XY):
      h = K
      XY.remove((x, y))
  return "Yes"

def main():
  N, M, H, K = [int(i) for i in input().split()]
  S = list(input())
  XY = set()
  for _ in range(M):
    x, y = [int(i) for i in input().split()]
    XY.add((x, y))
  print(f(N, M, H, K, S, XY))

if __name__=="__main__":
  main()
