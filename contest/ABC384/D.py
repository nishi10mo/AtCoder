# Repeated Sequence
def f(N, S, A):
    candidates = set()
    for i in range(len(A)):
        for j in range(i + 1, len(A) + 1):
            candidates.add(sum(A[i:j]))
    maxA = sum(A)
    if S <= maxA:
        if S in candidates:
            return "Yes"
    r = S % maxA
    if r in candidates:
        return "Yes"
    return "No"

def main():
    N, S = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    print(f(N, S, A))

if __name__ == '__main__':
    main()
