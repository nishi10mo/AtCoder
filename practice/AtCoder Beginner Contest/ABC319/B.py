# Measure
def f(N):
    divisors = []
    for i in range(1, 10):
        if N%i == 0:
            divisors.append(i)
    divisors_N = []
    for i in divisors:
        divisors_N.append(N//i)
    results = []
    results.append(1)
    for i in range(1,N+1):
        ans = []
        for n_j in divisors_N:
            if i%n_j == 0:
                ans.append(N//n_j)
        if len(ans) == 0:
            ans = "-"
        else:
            ans = min(ans)
        results.append(ans)
    results = [str(i) for i in results]
    return results

def main():
    N = int(input())
    print("".join(f(N)))

if __name__=="__main__":
    main()
