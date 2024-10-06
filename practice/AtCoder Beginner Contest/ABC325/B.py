# World Meeting
def f(N, WX):
    ans = 0
    for i in range(N):
        standard = WX[i][1]
        num = 0
        for j in range(N):
            start_time = 9 + (WX[j][1] - standard)
            if 24 <= start_time:
                start_time -= 24
            elif start_time < 0:
                start_time += 24
            if 9 <= start_time <= 17:
                num += WX[j][0]
        ans = max(ans, num)
    return ans

def main():
    N = int(input())
    WX = []
    for _ in range(N):
        wx = [int(i) for i in input().split()]
        WX.append(wx)
    print(f(N, WX))

if __name__=="__main__":
    main()
