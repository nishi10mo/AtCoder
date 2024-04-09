import sys

def div2(x):
  y = x % 2
  return y 

def shiftOnly(a, n):
  c = 0
  a_ = list(map(div2, a))
  if n == a_.count(0):
    c += 1
    shiftOnly(a_)
  else:
    return c

n = input()
a = input()
a = int(a.strip(str(a)))
a = [int(i) for i in list(str(a))]
print(shiftOnly(a, n))
