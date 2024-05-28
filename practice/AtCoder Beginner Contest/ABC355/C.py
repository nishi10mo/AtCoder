# Bingo 2
def calc(N, T, A):
  row = [0]*N
  col = [0]*N
  diag = [0]*2
  for i in range(T):
    x = A[i]//N
    y = A[i]%N

    row[x] += 1
    if row[x] == N:
      return i+1
    
    col[y] += 1
    if col[y] ==N:
      return i+1
    
    if x==y:
      diag[0] += 1
      if diag[0] == N:
        return i+1
    
    if x+y == N-1:
      diag[1] += 1
      if diag[1] == N:
        return i+1
  
  return -1

def main():
  N, T = [int(i) for i in input().split()]
  A = [int(i)-1 for i in input().split()]
  print(calc(N, T, A))

if __name__=="__main__":
  main()
