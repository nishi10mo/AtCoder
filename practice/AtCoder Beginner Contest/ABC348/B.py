# Farthest Point
import math

def calc(N, XY):
    dis_ = [0]*N
    dis = []
    for i in range(N):
        dis.append(dis_)
    ans = []
    for i in range(N):
        for j in range(N):
            dis[i][j] = math.sqrt((XY[i][0]-XY[j][0])**2 + (XY[i][1]-XY[j][1])**2)
        tmp = max(dis[i])
        index = dis[i].index(tmp) + 1
        ans.append(index)
    return ans

def main():
    N = int(input())
    XY = []
    for i in range(N):
        XY_ = [int(i) for i in input().split()]
        XY.append(XY_)
    ans = calc(N, XY)
    for i in range(N):
        print(ans[i])

if __name__=="__main__":
    main()
