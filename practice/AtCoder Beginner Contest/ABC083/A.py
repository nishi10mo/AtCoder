def Libra(a, b, c, d):
  left = a + b
  right = c + d
  if left > right:
    return "Left"
  elif left == right:
    return "Balanced"
  else:
    return "Right"

a, b, c, d = list(map(int, input().split()))
print(Libra(a, b, c, d))
