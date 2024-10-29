# MissingNo.
def f(N, A):
    A = sorted(A)
    start = min(A)
    end = start + N + 1
    all_list = [i for i in range(start, end)]
    for i in range(N):
        if A[i] != all_list[i]:
            return all_list[i]

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    print(f(N, A))

if __name__=="__main__":
    main()
