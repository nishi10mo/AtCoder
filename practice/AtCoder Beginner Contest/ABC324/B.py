# 3-smooth Numbers
def f(N):
    while N%2 == 0:
        N = N//2
    while N%3 == 0:
        N = N//3
    if N == 1:
        return "Yes"
    return "No"

def main():
    N = int(input())
    print(f(N))

if __name__=="__main__":
    main()
