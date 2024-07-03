# Error Correction
def f(N, T, S):

  def checkequal(s):
    if s == T:
      return True
    else:
      return False
  
  def checkinsert(s):
    p = 0
    t = 0
    n = len(s)
    if n != len(T)+1:
      return False
    for i in range(n):
      if s[i] == T[t]:
        t += 1
        if t == len(T):
          return True
      else:
        p += 1
    if p == 1:
      return True
    else:
      return False
  
  def checkdelete(s):
    p = 0
    n = 0
    if len(s) != len(T)-1:
      return False
    for i in range(len(T)):
      if T[i] == s[n]:
        n += 1
        if n == len(s):
          return True
      else:
        p += 1
    if p == 1:
      return True
    else:
      return False
  
  def checkreplace(s):
    p = 0
    t = 0
    n = len(s)
    if n != len(T):
      return False
    for i in range(n):
      if s[i] != T[t]:
        p += 1
      t += 1
    if p == 1:
      return True
    else:
      return False

  ans = []
  for i, s in enumerate(S):
    flag = checkequal(s)
    if flag == True:
      ans.append(i+1)
      continue
    flag = checkinsert(s)
    if flag == True:
      ans.append(i+1)
      continue
    flag = checkdelete(s)
    if flag == True:
      ans.append(i+1)
      continue
    flag = checkreplace(s)
    if flag == True:
      ans.append(i+1)
      continue
  
  length = len(ans)
  return length, ans

def main():
  N, T = [i for i in input().split()]
  N = int(N)
  T = list(T)
  S = []
  for _ in range(N):
    s = list(input())
    S.append(s)
  length, ans = f(N, T, S)
  print(length)
  print(*ans)

if __name__=="__main__":
  main()
  