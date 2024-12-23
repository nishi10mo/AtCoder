# Alternately
def f(N, S):
    pre = S[0]
    for i in range(1, N):
        if pre == S[i]:
            return "No"
        pre = S[i]
    return "Yes"

def main():
    N = int(input())
    S = list(input())
    print(f(N, S))

if __name__ == '__main__':
    main()
