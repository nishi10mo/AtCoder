def f(N, p):
    results = [0]*N
    for i in range(N):
        results[(p[i]-i)%N] += 1
        results[(p[i]-i-1)%N] += 1
        results[(p[i]-i+1)%N] += 1
    return max(results)

def main():
    N = int(input())
    p = [int(i) for i in input().split()]
    print(f(N, p))

if __name__ == '__main__':
    main()