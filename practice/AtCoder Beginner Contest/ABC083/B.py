def SomeSums(n, a, b):
  result = 0
  for i in range(1, n+1):
    num = list(map(int, list(str(i))))
    total = sum(num)
    if a <= total <= b:
      result += i
  return result

n, a, b = input().split()
n = int(n)
a = int(a)
b = int(b)
print(SomeSums(n, a, b))
