# 高橋君とお肉
def main():
  n = int(input())
  t = []
  for i in range(n):
    t_ = int(input())
    t.append(t_)

  rec = []
  for bit in range(1 << n):
    a = 0
    b = 0
    for i in range(n):
      if bit >> i & 1:
        a += t[i]
      else:
        b += t[i]
    rec.append(max(a, b))
  print(min(rec))

if __name__=="__main__":
  main()
