# Cash Register
def f(S):
    ans = 0
    while len(S) != 0:
        back = S[-1]
        S = S[:-1]
        if back == "0" and S[-1] == "0":
            S = S[:-1]
        ans += 1
    return ans

def main():
    S = input()
    print(f(S))

if __name__=="__main__":
    main()
