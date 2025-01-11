# Heavy Snake
def f(N, D, T, L):
    results = []
    for k in range(1, D+1):
        weights = []
        for i in range(N):
            weights.append(T[i]*(k+L[i]))
        weights = sorted(weights, reverse=True)
        results.append(weights[0])
    return results

def main():
    N, D = [int(i) for i in input().split()]
    T = []
    L = []
    for _ in range(N):
        t, l = [int(i) for i in input().split()]
        T.append(t)
        L.append(l)
    results = f(N, D, T, L)
    for ans in results:
        print(ans)

if __name__ == '__main__':
    main()
