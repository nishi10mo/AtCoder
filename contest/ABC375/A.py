# Seats
def f(N, S):
    c = 0
    for i in range(N-2):
        if S[i] == "#" and S[i+1]=="." and S[i+2]=="#":
            c += 1
    return c

def main():
    N = int(input())
    S = list(input())
    print(f(N, S))

if __name__=="__main__":
    main()
