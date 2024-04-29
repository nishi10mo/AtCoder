def SkillUp(N, M, X, C, A):
  ans = 1e65
  for bit in range(1 << N):
    rec = [0]*M #各アルゴリズムの理解度を記録
    tmp = 0 #各組合せにおける合計金額を記録
    for i in range(N):
      if bit >> i & 1:
        tmp += C[i]
        for j in range(M):
          rec[j] += A[i][j]
    flag = True
    for i in rec:
      if i < X:
        flag = False
        break
    if flag==True and tmp < ans:
      ans = tmp
  if ans==1e65:
    ans = -1
  return ans

N, M, X = map(int, input().split())
CA = []
C = []
A = []
for i in range(N):
  CA_ = list(map(int, input().split()))
  CA.append(CA_)
for row in CA:
  C.append(row[0])
  A.append(row[1:M+1])
print(SkillUp(N, M, X, C, A))

