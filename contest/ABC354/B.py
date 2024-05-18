# AtCoder Janken 2
def calc(N, S, C):
  S = sorted(S)
  total = sum(C)
  num = total%N
  return S[num]

def main():
  N = int(input())
  S = []
  C = []
  for i in range(N):
    S_, C_ = input().split()
    C_ = int(C_)
    S.append(S_)
    C.append(C_)
  print(calc(N, S, C))

if __name__=="__main__":
  main()
