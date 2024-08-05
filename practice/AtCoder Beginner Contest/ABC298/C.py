# Cards Query Problem
def f(N, Q, query):
  card = {}
  box = {}
  result = []
  for q in query:
    if q[0]==1:
      try:
        card[q[1]].add(q[2])
      except:
        card[q[1]] = set([q[2]])
      try:
        box[q[2]].append(q[1])
      except:
        box[q[2]] = [q[1]]
    elif q[0]==2:
      ans = sorted(box[q[1]])
      result.append(ans)
    else:
      ans = sorted(card[q[1]])
      result.append(ans)
  return result

def main():
  N = int(input())
  Q = int(input())
  query = []
  for _ in range(Q):
    q = [int(i) for i in input().split()]
    query.append(q)
  result = f(N, Q, query)
  for ans in result:
    print(*ans)

if __name__=="__main__":
  main()
