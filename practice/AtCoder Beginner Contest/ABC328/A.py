# Not Too Hard
def f(N, X, S):
    ans = 0
    for s in S:
        if s <= X:
            ans += s
    return ans

def main():
    N, X = [int(i) for i in input().split()]
    S = [int(i) for i in input().split()]
    print(f(N, X, S))

if __name__=="__main__":
    main()
