# Find snuke
def f(H, W, S):
    def fivecheck(x, y):
        target = ["s", "n", "u", "k", "e"]
        for i in range(5):
            if S[x+i][y:y+5] == target:
                return 

def main():
    H, W = [int(i) for i in input().split()]
    S = []
    for _ in range(H):
        s = list(input())
        S.append(s)
