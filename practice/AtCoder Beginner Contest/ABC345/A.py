# Leftrightarrow
def calc(S):
  n = len(S)
  if n < 3 or S[0]!="<" or S[-1]!=">":
    return "No"
  for i in range(1, n-1):
    if S[i]!="=":
      return "No"
  return "Yes"

def main():
  S = list(input())
  print(calc(S))

if __name__=="__main__":
  main()
