# quicksort
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

