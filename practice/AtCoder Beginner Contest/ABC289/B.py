# レ
def f(N, M, a):
  c = 0
  results = [i for i in range(1, N+1)]
  if M == 0:
    return results
  pre = a[0]
  for i in a:
    if i == pre+1:
      c += 1
    else:
      c = 0
    results.insert(i-c-1, i+1)
    del results[i+1]
    pre = i
  return results

def main():
  N, M = [int(i) for i in input().split()]
  a = [int(i) for i in input().split()]
  print(" ".join([str(i) for i in f(N, M, a)]))

if __name__ == '__main__':
  main()
