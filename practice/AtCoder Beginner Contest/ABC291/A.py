# camel Case
def f(S):
    n = len(S)
    for i in range(n):
        if S[i].isupper():
            return i+1

def main():
    S = list(input())
    print(f(S))

if __name__ == '__main__':
    main()
