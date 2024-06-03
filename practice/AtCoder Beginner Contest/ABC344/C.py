# A+B+C
def output(N, A, M, B, L, C, Q, X):
    cand = set()
    ans = []
    for i in A:
        for j in B:
            for k in C:
                tmp = i + j + k
                cand.add(tmp)
    for x in X:
        if x in cand:
            ans.append("Yes")
        else:
            ans.append("No")
    return ans

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    M = int(input())
    B = [int(i) for i in input().split()]
    L = int(input())
    C = [int(i) for i in input().split()]
    Q = int(input())
    X = [int(i) for i in input().split()]
    ans = output(N, A, M, B, L, C, Q, X)
    for i in ans:
        print(i)

if __name__=="__main__":
    main()
