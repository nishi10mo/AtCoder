# Cuboid Sum Query
def f(N, A, Q, L):
    A_ = [[[0]*N for _ in range(N)] for _ in range(N)]
    i = 0
    for x in range(N):
        for y in range(N):
            j = 0
            for z in range(N):
                A_[x][y][z] = A[i][j]
                j += 1
            i += 1
    A = A_
    result = []
    for l in L:
        tmp = 0
        for x in range(l[0]-1, l[1]):
            for y in range(l[2]-1, l[3]):
                for z in range(l[4]-1, l[5]):
                    tmp += A[x][y][z]
        result.append(tmp)
    return result

def main():
    N = int(input())
    A = []
    for _ in range(N**2):
        a = [int(i) for i in input().split()]
        A.append(a)
    Q = int(input())
    L = []
    for _ in range(Q):
        l = [int(i) for i in input().split()]
        L.append(l)
    result = f(N, A, Q, L)
    for ans in result:
        print(ans)

if __name__=="__main__":
    main()
