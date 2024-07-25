# Centers 
def f(N, A):
  dic = {}
  for i in range(N):
    dic[i+1] = []
  for i, v in enumerate(A):
    dic[v].append(i+1)
  order = []
  for i in range(N):
    order.append([i+1, dic[i+1][1]])
  order = sorted(order, key=lambda x:x[1])
  results = [i[0] for i in order]
  return results

def main():
  N = int(input())
  A = [int(i) for i in input().split()]
  results = f(N, A)
  print(*results)

if __name__=="__main__":
  main()

