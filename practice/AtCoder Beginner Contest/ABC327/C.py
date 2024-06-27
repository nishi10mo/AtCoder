# Number Place
def f(A):
  # check rows
  for row in A:
    setrow = set(row)
    if len(setrow) != 9:
      return "No"
  
  # check columns
  for i in range(9):
    col = set()
    for j in range(9):
      col.add(A[j][i])
    if len(col) != 9:
      return "No"
  
  # check 3*3 regions
  for i in range(3):
    for j in range(3):
      reg = set()
      for k in range(3*i, 3*i+3):
        for s in range(3*j, 3*j+3):
          reg.add(A[k][s])
      if len(reg) != 9:
        return "No"
  
  return "Yes"

def main():
  A = []
  for _ in range(9):
    a = [int(i) for i in input().split()]
    A.append(a)
  print(f(A))

if __name__=="__main__":
  main()
