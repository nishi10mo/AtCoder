# chess960
def f(S):
    b = []
    k = []
    r = []
    n = len(S)
    for i in range(n):
        if S[i] == "B":
            b.append(i)
        elif S[i] == "K":
            k.append(i)
        elif S[i] == "R":
            r.append(i)
    if (b[0]%2 + b[1]%2)%2 == 0:
        return "No"
    if r[0] < k[0] < r[1]:
        return "Yes"
    else:
        return "No"

def main():
    S = list(input())
    print(f(S))

if __name__ == '__main__':
    main()
