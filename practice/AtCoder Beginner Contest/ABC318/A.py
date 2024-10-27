# Full Moon
def f(N, M, P):
    ans = 0
    n = M
    while True:
        if n > N:
            break
        ans += 1
        n += P
    return ans

def main():
    N, M, P = [int(i) for i in input().split()]
    print(f(N, M, P))

if __name__=="__main__":
    main()
