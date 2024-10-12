# Spiral Rotation
import copy
def f(N, A):
    for i in range(N//2):
        B = copy.deepcopy(A)
        for x in range(i, N-i):
            for y in range(i, N-i):
                 B[y][N-x-1] = A[x][y]
        A = B
    return B

def main():
    N = int(input())
    A = [[""]*N for _ in range(N)]
    for x in range(N):
        a = list(input())
        for y in range(N):
            A[x][y] = a[y]
    B = f(N, A)
    for b in B:
        print("".join(b))

if __name__=="__main__":
    main()
