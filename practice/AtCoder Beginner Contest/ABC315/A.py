# tcdr
def f(S):
    ans = [s for s in S if s != "a" and s != "i" and s != "u" and s != "e" and s != "o"]
    return "".join(ans)

def main():
    S = list(input())
    print(f(S))

if __name__=="__main__":
    main()
