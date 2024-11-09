# Cyclic
def f(N):
    ans1 = [str(i) for i in [N[1], N[2], N[0]]]
    ans1 = int("".join(ans1))
    ans2 = [str(i) for i in [N[2], N[0], N[1]]]
    ans2 = int("".join(ans2))
    return ans1, ans2

def main():
    N = [int(i) for i in list(input())]
    print(*f(N))

if __name__=="__main__":
    main()
