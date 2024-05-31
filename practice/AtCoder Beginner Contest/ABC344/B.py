# Delimiter
def main():
  A = []
  while True:
    a = int(input())
    A.append(a)
    if a == 0:
      break
  n = len(A)
  for i in range(n-1, -1, -1):
    print(A[i])

if __name__=="__main__":
  main()