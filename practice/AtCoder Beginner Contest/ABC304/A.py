# First Player
def f(N, S, A):
    minv = min(A)
    mini = A.index(minv)
    SS = S + S
    ans = []
    for s in range(mini, mini+N):
        ans.append(SS[s])
    return ans

def main():
    N = int(input())
    S = []
    A = []
    for _ in range(N):
        s, a = list(input().split())
        S.append(s)
        A.append(int(a))
    results = f(N, S, A)
    for ans in results:
        print(ans)

if __name__=="__main__":
    main()
