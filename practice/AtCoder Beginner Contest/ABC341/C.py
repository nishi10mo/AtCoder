# Takahashi Gets Lost
import copy

def calc(H, W, N, T, S):
  ans = 0
  for i in range(H):
    for j in range(W):
      if S[i][j]=="#":
        continue
      I, J = i, j
      flag = True
      for t in T:
        if t == "L":
          J -= 1
        if t == "R":
          J += 1
        if t == "U":
          I -= 1
        if t == "D":
          I += 1
        if I<0 or I>=H or J<0 or J>=W or S[I][J]=="#":
          flag = False
          break
      if flag == True:
        ans += 1
  return ans

def main():
    H, W, N = [int(i) for i in input().split()]
    T = list(input())
    S = []
    for _ in range(H):
        s = list(input())
        S.append(s)
    print(calc(H, W, N, T, S))

if __name__=="__main__":
  main()
