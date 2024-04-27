def TheBottomOfTheNinth(a, b):
  suma = sum(a)
  sumb = sum(b)
  if sumb - suma > 0:
    return 0
  else:
    return suma - sumb + 1

a = list(map(int, list(input().split())))
b = list(map(int, list(input().split())))
print(TheBottomOfTheNinth(a, b))
