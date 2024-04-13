def rem2(x):
  y = x % 2
  return y

def div2(x):
  y = x//2
  return y

def shiftOnly(a, n):
  c = 0
  a_next = a.copy()
  a_ = list(map(rem2, a_next))
  while n == a_.count(0):
    c += 1
    a = list(map(div2, a))
    a_next = a.copy()
    a_ = list(map(rem2, a_next))
  return c

n = int(input())
a = list(map(int, input().split()))
print(shiftOnly(a, n))
