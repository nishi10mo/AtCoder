# ab
def f(N, S):
    for i in range(N-1):
        if S[i] == "a":
            if S[i+1] == "b":
                return "Yes"
        if S[i] == "b":
            if S[i+1] == "a":
                return "Yes"
    return "No"

def main():
    N = int(input())
    S = input()
    print(f(N, S))

if __name__=="__main__":
    main()
