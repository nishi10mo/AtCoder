# Scoreboard 
def f(N, XY):
    takahashi = 0
    aoki = 0
    for xy in XY:
        takahashi += xy[0]
        aoki += xy[1]
    if takahashi > aoki:
        return "Takahashi"
    elif takahashi < aoki:
        return "Aoki"
    else:
        return "Draw"

def main():
    N = int(input())
    XY = []
    for _ in range(N):
        xy = [int(i) for i in input().split()]
        XY.append(xy)
    print(f(N, XY))

if __name__=="__main__":
    main()
