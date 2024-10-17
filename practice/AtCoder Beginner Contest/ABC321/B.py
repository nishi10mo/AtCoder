# Cutoff
def f(N, X, A):
    minA = min(A)
    maxA = max(A)
    if len(A) == 2:
        if maxA < X:
            return -1
        else:
            if minA >= X:
                return 0
            else:
                return X
    A = sorted(A)
    total = sum(A[1:-1])
    if total >= X:
        return 0
    rem = X - total
    if rem <= minA:
        return 0
    elif minA < rem <= maxA:
        return rem
    else:
        return -1

def main():
    N, X = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    print(f(N, X, A))

if __name__=="__main__":
    main()
