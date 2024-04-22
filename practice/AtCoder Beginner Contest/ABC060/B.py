def ChooseIntegers(a, b, c):
  for i in range(0, b+1):
    rem = a*i%b
    if rem==c:
      return "YES"
  return "NO"

a, b, c = list(map(int, list(input().split())))
print(ChooseIntegers(a, b, c))
