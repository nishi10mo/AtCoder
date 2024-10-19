# Prepare Another Box
def f(N, A, B):
    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)
    c = 0
    for i in range(N-1):
        if (A[i] > B[i]) and (c == 0):
            ans = A[i]
            B.insert(i, A[i])
            c += 1
        elif (A[i] > B[i]) and (c != 0):
            return -1
    if c == 0:
        return A[N-1]
    if A[N-1] > B[N-1]:
        return -1
    return ans    

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    print(f(N, A, B))

if __name__=="__main__":
    main()
