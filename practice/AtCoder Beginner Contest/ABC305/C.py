# Snuke the Cookie Picker
def f(H, W, S):
  U = 10**18
  D = -10**18
  L = 10 **18
  R = -10**18
  for i in range(H):
    for j in range(W):
      if S[i][j]=="#":
        U = min(U, i)
        D = max(D, i)
        L = min(L, j)
        R = max(R, j)
  for i in range(U, D+1):
    for j in range(L, R+1):
      if S[i][j]==".":
        return [i+1, j+1]


def main():
  H, W = [int(i) for i in input().split()]
  S = []
  for _ in range(H):
    s = list(input())
    S.append(s)
  print(*f(H, W, S))

if __name__=="__main__":
  main()
