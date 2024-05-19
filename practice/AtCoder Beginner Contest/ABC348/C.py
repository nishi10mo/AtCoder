# Colorful Beans
# 以下の開放はTLE
# def calc(N, A, C):
#   ans_cand = []
#   ans = 0
#   colors = set(C)
#   for i in colors:
#     for j in range(N):
#       if i == C[j]:
#         ans_cand.append(A[j])
#     ans_ = min(ans_cand)
#     ans = max(ans_, ans)
#     ans_cand = []
#   return ans

def calc(N, A, C):
  ans_cand = {}
  for i in range(N):
    if C[i] in ans_cand:
      ans_cand[C[i]] = min(ans_cand[C[i]], A[i])
    else:
      ans_cand[C[i]] = A[i]
  ans = max(ans_cand.values())
  return ans

def main():
  N = int(input())
  A = []
  C = []
  for i in range(N):
    A_, C_ = [int(i) for i in input().split()]
    A.append(A_)
    C.append(C_)
  print(calc(N, A, C))

if __name__=="__main__":
  main()
