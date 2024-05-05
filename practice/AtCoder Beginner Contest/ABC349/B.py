# Commencement
import sys

def main():
  S = list(input())
  S_ = list(set(S))
  n = len(S_)
  c=[]
  for i in range(n):
    tmp = S.count(S_[i])
    c.append(tmp)
  m = max(c)
  for i in range(m):
    tmp = c.count(i+1)
    if tmp!=0 and tmp!=2:
      print("No")
      exit()
  print("Yes")

if __name__=="__main__":
  main()
