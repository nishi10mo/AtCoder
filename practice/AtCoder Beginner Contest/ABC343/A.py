# Wrong Answer
def f(A, B):
  tmp = A + B
  if tmp == 0:
    return 1
  else:
    return 0

def main():
  A, B = [int(i) for i in input().split()]
  print(f(A, B))

if __name__=="__main__":
  main()
