# First ABC
def f(N, S):
    a = 0
    b = 0
    c = 0
    for i in range(N):
        if S[i] == "A":
            a += 1
        elif S[i] == "B":
            b += 1
        elif S[i] == "C":
            c += 1
        if a > 0 and b > 0 and c > 0:
            return i + 1

def main():
    N = int(input())
    S = list(input())
    print(f(N, S))

if __name__=="__main__":
    main()
