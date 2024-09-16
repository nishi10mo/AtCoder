# String Delimiter
def f(N, S):
    quotation = "zero"
    for i in range(N):
        if S[i] == ',' and quotation == "zero":
            S[i] = "."
        elif  S[i] == '"' and quotation == "zero":
            quotation = "first"
        elif S[i] == '"' and quotation == "first":
            quotation = "zero"
    return S

def main():
    N = int(input())
    S = list(input())
    print("".join(f(N, S)))

if __name__=="__main__":
    main()
