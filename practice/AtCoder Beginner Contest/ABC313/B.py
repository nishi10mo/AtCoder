# Who is Saikyo?
def f(N, M, A, B):
    ans = []
    cand = list(set(A))
    for i in cand:
        if i in B:
            continue
        else:
            ans.append(i)
    if len(ans) == 1:
        return ans[0]
    else:
        return -1

def main():
    N, M = [int(i) for i in input().split()]
    A = []
    B = []
    for _ in range(M):
        a, b = [int(i) for i in input().split()]
        A.append(a)
        B.append(b)
    print(f(N, M, A, B))

if __name__=="__main__":
    main()
