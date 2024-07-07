# Yay!
def f(S):
  if S[0] == S[1]:
    same = S[0]
  else:
    if S[0] == S[2]:
      return 2
    else:
      return 1
  for i in range(2, len(S)):
    if S[i] != same:
      return i+1

def main():
  S = list(input())
  print(f(S))

if __name__=="__main__":
  main()
