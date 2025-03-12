# Cat 

def f(N, S):
    pre = S[0]
    for i in range(1, N):
        if pre == "n" and S[i] == "a":
            S[i] = "ya"
            pre = "a"
        else:
            pre = S[i]
    return "".join(S)

def main():
    N = int(input())
    S = list(input())
    print(f(N, S))

if __name__=="__main__":
    main()
