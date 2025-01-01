# Filter
def f(N, A):
    results = []
    for a in A:
        if a%2 == 0:
            results.append(a)
    return " ".join([str(i) for i in results])

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    print(f(N, A))

if __name__ == '__main__':
    main()

