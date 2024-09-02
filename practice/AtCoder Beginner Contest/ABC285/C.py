# abc285_brutmhyhiizp
def f(S):
    n = len(S)
    ans = 0
    for s in S:
        n -= 1
        num = ord(s) - ord("A") + 1
        ans += (26**n)*num
    return ans

def main():
    S = list(input())
    print(f(S))

if __name__=="__main__":
    main()
