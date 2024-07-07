# Blue Spring
def f(N, D, P, F):
  results = []
  F = sorted(F, reverse=True)
  flag = True
  while flag==True:
    if len(F) > D:
      Fl = F[:D]
    else:
      Fl = F
    if sum(Fl) > P:
      results += [P]
      F = F[D:]
    else:
      results += F
      flag = False
  return sum(results)

def main():
  N, D, P = [int(i) for i in input().split()]
  F = [int(i) for i in input().split()]
  print(f(N, D, P, F))

if __name__=="__main__":
  main()
