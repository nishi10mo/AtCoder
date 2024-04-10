def bcOnly(b, c, rem, count):
  b_ = rem//100
  if b_ >= b:
    b_ = b
  while b_ >= 0:
    rem_ = rem - 100*b_
    c_ = rem_//50
    if c_ <= c:
      count += 1
    else:
      break
    b_ -= 1
  return count

def Coins(a, b, c, x):
  count = 0
  a_ = x//500
  if a_ >= a:
    a_ = a
  while a_ >= 0:
    rem = x - 500*a_
    count = bcOnly(b, c, rem, count)
    a_ -= 1
  return count

a = int(input())
b = int(input())
c = int(input())
x = int(input())
print(Coins(a, b, c, x))
