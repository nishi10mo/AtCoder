# Blue Spring
# 以下はTLE
# def f(N, D, P, F):
#   results = []
#   F = sorted(F, reverse=True)
#   flag = True
#   while flag==True:
#     if len(F) > D:
#       Fl = F[:D]
#     else:
#       Fl = F
#     if sum(Fl) > P:
#       results += [P]
#       F = F[D:]
#     else:
#       results += F
#       flag = False
#   return sum(results)

def f(N, D, P, F):
  F = sorted(F)
  cumsum = [0]*N
  cumsum[0] = F[0]
  for i in range(1, N):
    cumsum[i] = cumsum[i-1] + F[i]
  k = (N + D - 1) // D
  ans = P*k
  for i in range(k):
    ans = min(ans, cumsum[N-1-(i*D)]+(P*i))
  return ans

def main():
  N, D, P = [int(i) for i in input().split()]
  F = [int(i) for i in input().split()]
  print(f(N, D, P, F))

if __name__=="__main__":
  main()
