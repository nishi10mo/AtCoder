# 2UP3DOWN
def f(X, Y):
  if -3 <= (Y - X) <= 2:
    return "Yes"
  else:
    return "No"

def main():
  X, Y = [int(i) for i in input().split()]
  print(f(X, Y))

if __name__=="__main__":
  main()
