# AtCoder Cards
from collections import defaultdict
def f(S, T):
    Sc = defaultdict(int)
    Tc = defaultdict(int)
    for i in S:
        Sc[i] += 1
    for i in T:
        Tc[i] += 1
    for c in "atcoder":
        M = max(Sc[c], Tc[c])
        if (M-Sc[c] > Sc["@"]) or (M-Tc[c] > Tc["@"]):
            return "No"
        Sc["@"] -= M-Sc[c]
        Sc[c] = M
        Tc["@"] -= M-Tc[c]
        Tc[c] = M
    if Sc == Tc:
        return "Yes"
    else:
        return "No"

def main():
    S = input()
    T = input()
    print(f(S, T))

if __name__=="__main__":
    main()
