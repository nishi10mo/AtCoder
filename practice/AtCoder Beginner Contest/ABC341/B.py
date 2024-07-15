# Foreign Exchange
def f(N, A, S, T):
  for i in range(N-1):
    tmp = A[i]//S[i]
    A[i] -= tmp*S[i]
    A[i+1] += tmp*T[i]
  return A[N-1]

def main():
  N = int(input())
  A = [int(i) for i in input().split()]
  S = []
  T = []
  for _ in range(N-1):
    s, t = [int(i) for i in input().split()]
    S.append(s)
    T.append(t)
  print(f(N, A, S, T))

if __name__=="__main__":
  main()
  