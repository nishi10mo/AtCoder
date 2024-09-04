# Online Shopping
def f(N, S, K, PQ):
    total = 0
    for pq in PQ:
        p, q = pq
        total += p*q
    if total >= S:
        return total
    else:
        return total + K

def main():
    N, S, K = [int(i) for i in input().split()]
    PQ = []
    for _ in range(N):
        pq = [int(i) for i in input().split()]
        PQ.append(pq)
    print(f(N, S, K, PQ))

if __name__=="__main__":
    main()
    
