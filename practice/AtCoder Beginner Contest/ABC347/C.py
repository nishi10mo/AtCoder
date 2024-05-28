# Ideal Holidays
def calc(N, A, B, D):
  week = A + B
  for i in range(week):
    D_ = [(i+j)%week for j in D]
    diff = max(D_) - min(D_)
    if diff < A:
      return "Yes"
  return "No"

def main():
  N, A, B = [int(i) for i in input().split()]
  D = [int(i) for i in input().split()]
  print(calc(N, A, B, D))

if __name__=="__main__":
  main()
