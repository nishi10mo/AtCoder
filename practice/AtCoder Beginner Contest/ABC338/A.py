# Capitalized?
def f(S):
  flag = "No"
  N = len(S)
  if S[0].islower():
    return "No"
  if S[0].isupper() and N==1:
    return "Yes"
  for i in range(1, N):
    if S[i].isupper():
      return "No"
  return "Yes"

def main():
  S = input()
  print(f(S))

if __name__=="__main__":
  main()
