# Append 
def f(Q, query):
  A = []
  results = []
  for q in query:
    if q[0]==1:
      A.append(q[1])
    else:
      results.append(A[-q[1]])
  return results

def main():
  Q = int(input())
  query = []
  for _ in range(Q):
    q = [int(i) for i in input().split()]
    query.append(q)
  results = f(Q, query)
  for ans in results:
    print(ans)

if __name__=="__main__":
  main()
  
