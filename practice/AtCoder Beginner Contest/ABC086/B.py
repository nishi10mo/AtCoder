import math

def OneTwoOne(a, b):
  x = int(a + b)
  if math.sqrt(x).is_integer():
    return "Yes"
  else:
    return "No"

a, b = list(input().split())
print(OneTwoOne(a, b))

