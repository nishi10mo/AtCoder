def SumofThreeIntegers(k, s):
  c = 0 #何通りあるかを数える変数
  for p in range(k+1):
    for q in range(k+1):
      rem = s - p - q
      if 0 <= rem <= k:
        c += 1
  return c

k, s = list(map(int, list(input().split())))
print(SumofThreeIntegers(k, s))
