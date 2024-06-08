# Many Replacement
from string import ascii_lowercase
def calc(N, S, Q, C, D):
  mapping_from = ascii_lowercase
  mapping_to = ascii_lowercase
  for i in range(Q):
    mapping_to = mapping_to.replace(C[i], D[i])
  dict = str.maketrans(mapping_from, mapping_to)
  S = S.translate(dict)
  return S

def main():
  N = int(input())
  S = input()
  Q = int(input())
  C = []
  D = []
  for _ in range(Q):
    c, d = input().split()
    C.append(c)
    D.append(d)
  print(calc(N, S, Q, C, D))

if __name__=="__main__":
  main()
