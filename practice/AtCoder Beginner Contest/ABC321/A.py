# 321-like Checker
def f(N):
    n = len(N)
    for i in range(n-1):
        if N[i] <= N[i+1]:
            return "No"
    return "Yes"

def main():
    N = [int(i) for i in list(input())]
    print(f(N))

if __name__=="__main__":
    main()
