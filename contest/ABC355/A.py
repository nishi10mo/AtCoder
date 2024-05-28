# Who Ate the Cake?
def calc(A, B):
  cand = set(range(1, 4))
  AB = set([A, B])
  ans = cand - AB
  ans = list(ans)
  if len(ans) == 2:
    return -1
  else:
    return ans[0]

def main():
  A, B = [int(i) for i in input().split()]
  print(calc(A, B))

if __name__=="__main__":
  main()
