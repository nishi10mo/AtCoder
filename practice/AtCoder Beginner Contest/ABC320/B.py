# Longest Palindrome
def f(S):
    n = len(S)
    for i in range(n, 0, -1):
        for j in range(n-i+1):
            S_part = S[j:i+j]
            S_part_reverse = list(reversed(S_part))
            if S_part == S_part_reverse:
                return i

def main():
    S = list(input())
    print(f(S))

if __name__=="__main__":
    main()
