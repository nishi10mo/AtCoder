# Repeated Sequence
def f(N, S, A):
    S %= sum(A)
    A += A
    for i in range(1, 2*N):
        A[i] += A[i-1]
    A_set = set(A)
    for a in A:
        if S + a in A_set:
            return 'Yes'
    return 'No'

def main():
    N, S = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    print(f(N, S, A))

if __name__ == '__main__':
    main()
