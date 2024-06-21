# Repunit Trio
def f(N):
  L = 12
  r = [int("1"*(i+1)) for i in range(L)]
  s = set()
  for i in range(L):
    for j in range(L):
      for k in range(L):
        s.add(r[i] + r[j] + r[k])
  s = sorted(s)
  return s[N-1]

def main():
  N = int(input())
  print(f(N))

if __name__=="__main__":
  main()
