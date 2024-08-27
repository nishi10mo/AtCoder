# CTZ
def f(N):
    ans = 0
    while N%2 == 0:
        N = N//2
        ans += 1
    return ans

def main():
    N = int(input())
    print(f(N))

if __name__=="__main__":
    main()
