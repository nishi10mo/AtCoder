# Trimmed Mean
def f(N, X):
    x = sorted(X)
    return sum(x[N:-N])/len(x[N:-N])

def main():
    N = int(input())
    X = [int(i) for i in input().split()]
    print(f(N, X))

if __name__ == '__main__':
    main()
