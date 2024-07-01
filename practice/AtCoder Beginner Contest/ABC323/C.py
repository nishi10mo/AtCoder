# World Tour Finals
def f(N, M, A, S):
  score = []
  for i in range(N):
    tmp = i+1
    for j in range(M):
      if S[i][j] == "x":
        continue
      else:
          tmp += A[j]
    score.append(tmp)
  mx = max(score)
  results = []
  for i in range(N):
    rem = []
    for j in range(M):
      if S[i][j] == "x":
        rem.append(A[j])
    rem = sorted(rem, reverse=True)
    ans = 0
    while mx > score[i]:
      score[i] += rem[ans]
      ans += 1
    results.append(ans)
  return results

def main():
  N, M = [int(i) for i in input().split()]
  A = [int(i) for i in input().split()]
  S = []
  for _ in range(N):
    s = list(input())
    S.append(s)
  results = f(N, M, A, S)
  for ans in results:
    print(ans)

if __name__=="__main__":
  main()
