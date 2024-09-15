# Minimize Abs 1
def f(N, L, R, A):
    ans = []
    for a in A:
        if a <= L:
            ans.append(L)
        elif a >= R:
            ans.append(R)
        else:
            ans.append(a)
    return ans

def main():
    N, L, R = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    print(*f(N, L, R, A))

if __name__=="__main__":
    main()
