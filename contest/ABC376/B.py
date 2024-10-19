# Hands on Ring (Easy)
def f(N, Q, HT):
    l = 1
    r = 2
    for ht in HT:
        if ht[0] == "R":
            if r < ht[1]:
                


def main():
    N, Q = [int(i) for i in input().split()]
    HT = []
    for _ in range(Q):
        ht = [int(i) for i in input().split()]
        HT.append(ht)
