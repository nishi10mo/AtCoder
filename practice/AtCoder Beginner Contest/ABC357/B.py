# Uppercase and Lowercase
def output(S):
  arry = list(S)
  up = 0
  down = 0
  for s in S:
    if s.isupper():
      up += 1
    else:
      down += 1 
  if up > down:
    return S.upper()
  else:
    return S.lower()

def main():
    S = input()
    print(output(S))

if __name__=="__main__":
  main()
