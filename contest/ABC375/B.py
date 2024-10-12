# Traveling Takahashi Problem
from decimal import Decimal
def f(N, XY):
    dis = Decimal(XY[0][0]**2 + XY[0][1]**2).sqrt()
    for i in range(N-1):
        dis += Decimal((XY[i][0] - XY[i+1][0])**2 + (XY[i][1] - XY[i+1][1])**2).sqrt()
    dis += Decimal(XY[N-1][0]**2 + XY[N-1][1]**2).sqrt()
    return dis

def main():
    N = int(input())
    XY = []
    for _ in range(N):
        xy = [int(i) for i in input().split()]
        XY.append(xy)
    print(f(N, XY))

if __name__=="__main__":
    main()
