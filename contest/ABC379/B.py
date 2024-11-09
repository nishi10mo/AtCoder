# Strawberries
def f(N, K, S):
    pre = "X"
    now = 0
    ans = 0
    for s in S:
        if s == "O":
            now += 1
            if now == K:
                ans += 1
                now = 0
        else:
            now = 0
    return ans

def main():
    N, K = [int(i) for i in input().split()]
    S = list(input())
    print(f(N, K, S))

if __name__=="__main__":
    main()
