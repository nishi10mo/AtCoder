# Gap Existence
def f(N, X, A):
    A = set(A)
    for a in A:
        b = X + a
        if b in A:
            return "Yes"
    return "No"

def main():
    N, X = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    print(f(N, X, A))

if __name__=="__main__":
    main()
