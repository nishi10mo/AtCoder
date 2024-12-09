# Fill the Gaps
import copy

def f(N, A):
    results = copy.deepcopy(A)
    for i in range(N-1):
        if abs(A[i] - A[i+1]) == 1:
            continue
        else:
            if A[i] < A[i+1]:
                dis = A[i+1] - A[i]
                for j in range(dis-1):
                    results.insert(i+1+j, A[i]+1+j)
    
    i = 0
    while i < len(A)-1:
        if abs(A[i] - A[i+1]) != 1:
            if A[i] < A[i+1]:
                A.insert(i+1, A[i]+1)
            else:
                A.insert(i+1, A[i]-1)
        i += 1
    return A

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    print(*f(N, A))

if __name__=="__main__":
    main()
