# ARC Division
def f(N, R, D, A):
    for i in range(N):
        if D[i] == 1:
            if 1600 <= R and R <= 2799:
                R += A[i]
        else:
            if 1200 <= R and R <= 2399:
                R += A[i]
    return R

def main():
    N, R = [int(i) for i in input().split()]
    D = []
    A = []
    for _ in range(N):
        d, a = [int(i) for i in input().split()]
        D.append(d)
        A.append(a)
    print(f(N, R, D, A))

if __name__ == '__main__':
    main()
