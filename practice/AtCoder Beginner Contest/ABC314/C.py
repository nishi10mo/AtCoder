# Rotate Colored Subsequence
def f(N, M, S, C):
  count = [0]*M
  place = [0]*N
  for i, v in enumerate(C):
    count[v-1] += 1
    place[i] = count[v-1]

  
  align = [[] for _ in range(M)]
  return align
  for i in range(N):
    align[C[i]-1][place[i]-1] = S[i]
  return align

def main():
  N, M = [int(i) for i in input().split()]
  S = list(input())
  C = [int(i) for i in input().split()]
  print(f(N, M, S, C))

if __name__=="__main__":
  main()
