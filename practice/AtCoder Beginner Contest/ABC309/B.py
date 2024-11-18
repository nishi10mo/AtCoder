# Rotate
def f(N, A):
    B = []
    b = [A[1][0], *A[0][:N-1]]
    B.append(b)
    for i in range(1, N-1):
        b = [A[i+1][0], *A[i][1:N-1], A[i-1][N-1]]
        B.append(b)
    b = [*A[N-1][1:N], A[N-2][N-1]]
    B.append(b)
    return B

def main():
    N = int(input())
    A = []
    for _ in range(N):
        a = [int(i) for i in list(input())]
        A.append(a)
    B = f(N, A)
    for b in B:
        b = [str(i) for i in b]
        print("".join(b))

if __name__=="__main__":
    main()
