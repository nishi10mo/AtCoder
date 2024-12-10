# Overall Winner
def f(N, S):
    t = S.count("T")
    a = S.count("A")
    if t > a:
        return "T"
    elif t < a:
        return "A"
    else:
        t_n = 0
        a_n = 0
        for s in S:
            if s == "A":
                a_n += 1
            else:
                t_n += 1
            if a_n == a:
                return "A"
            if t_n == t:
                return "T"

def main():
    N = int(input())
    S = list(input())
    print(f(N, S))

if __name__=="__main__":
    main()
