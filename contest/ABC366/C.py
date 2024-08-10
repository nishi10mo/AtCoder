# Balls and Bag Query
from collections import defaultdict 
def f(Q, query):
    num = 0
    bag = defaultdict(int)
    result = []
    for q in query:
        if q[0]==1:
            if bag[q[1]]==0:
                num += 1
            bag[q[1]] += 1
        elif q[0]==2:
            bag[q[1]] -= 1
            if bag[q[1]]==0:
                num -= 1
        else:
            result.append(num)
    return result

def main():
    Q = int(input())
    query = []
    for _ in range(Q):
        q = [int(i) for i in input().split()]
        query.append(q)
    result = f(Q, query)
    for ans in result:
        print(ans)

if __name__=="__main__":
    main()
