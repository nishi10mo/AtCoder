# Swap Odd and Even
def f(S):
    n = len(S)
    for i in range(n):
        if i%2 == 0:
            S[i], S[i+1] = S[i+1], S[i]
    return "".join(S)

def main():
    S = list(input())
    print(f(S))

if __name__ == '__main__':
    main()
