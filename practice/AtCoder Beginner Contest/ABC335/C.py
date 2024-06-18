# Loong Tracking
import copy

def f(N, Q, query):
  dragon = {}
  for i in range(1, N+1):
    dragon[i] = [i, 0]
  ans = []
  for q in query:
    if q[0] == "1":
      if q[1] == "R":
        dragon_ = copy.deepcopy(dragon)
        dragon_[1][0] += 1
        for k in range(2, N+1):
          dragon_[k][0] = dragon[k-1][0]
          dragon_[k][1] = dragon[k-1][1]
        dragon = dragon_
      if q[1] == "L":
        dragon_ = copy.deepcopy(dragon)
        dragon_[1][0] -= 1
        for k in range(2, N+1):
          dragon_[k][0] = dragon[k-1][0]
          dragon_[k][1] = dragon[k-1][1]
        dragon = dragon_
      if q[1] == "U":
        dragon_ = copy.deepcopy(dragon)
        dragon_[1][1] += 1
        for k in range(2, N+1):
          dragon_[k][0] = dragon[k-1][0]
          dragon_[k][1] = dragon[k-1][1]
        dragon = dragon_
      if q[1] == "R":
        dragon_ = copy.deepcopy(dragon)
        dragon_[1][1] -= 1
        for k in range(2, N+1):
          dragon_[k][0] = dragon[k-1][0]
          dragon_[k][1] = dragon[k-1][1]
        dragon = dragon_
    elif q[0] == "2":
      ans.append(dragon[int(q[1])])
  return ans

def main():
  N, Q = [int(i) for i in input().split()]
  query = []
  for _ in range(Q):
    q = input().split()
    query.append(q)
  ans = f(N, Q, query)
  for a in ans:
    a = [str(i) for i in a]
    print(" ".join(a))
  
if __name__=="__main__":
  main()
  