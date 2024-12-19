# Job Interview
def f(N, S):
    ok = 0
    ng = 0
    for s in S:
        if s == "o":
            ok += 1
        elif s == "x":
            ng += 1
    if ok > 0 and ng == 0:
        return "Yes"
    return "No"

def main():
    N = int(input())
    S = list(input())
    print(f(N, S))

if __name__ == '__main__':
    main()
