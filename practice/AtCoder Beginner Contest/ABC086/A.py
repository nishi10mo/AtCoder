def Product(a, b):
  t = a*b%2
  if(t == 0):
    return "Even"
  else:
    return "Odd"

a, b = map(int, input().split())
print(Product(a, b))
