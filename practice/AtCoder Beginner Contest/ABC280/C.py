# Extra Character
def f(S, T):
    n = len(S)
    for i in range(n):
        if S[i] != T[i]:
            return i+1
    return len(T)

def main():
    S = list(input())
    T = list(input())
    print(f(S, T))

if __name__=="__main__":
    main()
