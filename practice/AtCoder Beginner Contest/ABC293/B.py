# Call the ID Number
def f(N, A):
    done = set()
    for i in range(N):
        if i+1 in done:
            pass
        else:
            done.add(A[i])
    results = []
    for i in range(1, N+1):
        if i in done:
            pass
        else:
            results.append(i)
    return results

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    results = f(N, A)
    print(len(results))
    print(" ".join([str(i) for i in results]))

if __name__ == '__main__':
    main()
