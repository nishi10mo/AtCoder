# Rotate Colored Subsequence
import copy
def f(N, M, S, C):
  count = [0]*M
  place = [0]*N
  for i, v in enumerate(C):
    count[v-1] += 1
    place[i] = count[v-1]

  align = []
  for i in count:
    tmp = [0]*i
    align.append(tmp)
  for i in range(N):
    align[C[i]-1][place[i]-1] = S[i]
  for i in align:
    i_ = copy.deepcopy(i)
    i += i_*2
  
  result =[]
  for i in range(N):
    ans = align[C[i]-1][place[i]+count[C[i]-1]-2]
    result.append(ans)
  return result

def main():
  N, M = [int(i) for i in input().split()]
  S = list(input())
  C = [int(i) for i in input().split()]
  result = f(N, M, S, C)
  print("".join(result))

if __name__=="__main__":
  main()
