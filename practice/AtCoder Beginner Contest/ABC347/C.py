# Ideal Holidays
def calc(N, A, B, D):
  week = A + B
  D = [i%week for i in D]
  D = sorted(list(set(D)))
  if len(D)==1:
    return "Yes"
  for i in range(len(D)):
    if i == len(D)-1:
      diff = (D[0]-D[i])%week
    else:
      diff = (D[i+1]-D[i])%week
    if diff > B:
      return "Yes"
  return "No"

def main():
  N, A, B = [int(i) for i in input().split()]
  D = [int(i) for i in input().split()]
  print(calc(N, A, B, D))

if __name__=="__main__":
  main()
