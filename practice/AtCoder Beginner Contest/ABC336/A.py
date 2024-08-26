# Long Loong
def f(N):
    ans = "L"
    for _ in range(N):
        ans += "o"
    ans += "n"
    ans += "g"
    return ans

def main():
    N = int(input())
    print(f(N))

if __name__=="__main__":
    main()
