def quicksort(seq):
  if len(seq) <= 1:
    return seq
  piv = seq[0]
  left = []
  right = []
  for i in range(1, len(seq)):
    if piv >= seq[i]:
      left.append(seq[i])
    else:
      right.append(seq[i])
  left = quicksort(left)
  right = quicksort(right)
  center = [piv]
  return left + center + right

def CardGameforTwo(n, a):
  a = quicksort(a)
  alice = []
  bob = []
  for i in range(n-1, -1, -2):
    alice.append(a[i])
  for i in range(n-2, -1, -2):
    bob.append(a[i])
  alice = sum(alice)
  bob = sum(bob)
  return alice - bob

n = int(input())
a = list(map(int, list(input().split())))
print(CardGameforTwo(n, a))
