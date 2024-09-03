# Three Threes
def f(N):
    ans = []
    str_n = str(N)
    for _ in range(N):
        ans.append(str_n)
    return "".join(ans)

def main():
    N = int(input())
    print(f(N))

if __name__=="__main__":
    main()
