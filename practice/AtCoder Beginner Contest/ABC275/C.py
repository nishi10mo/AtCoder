# Counting Squares
from itertools import combinations
def f(S):
    sharp = []
    for i in range(9):
        for j in range(9):
            if S[i][j]=="#":
                sharp.append((i, j))
    if len(sharp) < 4:
        return 0
    ans = 0
    for comb in combinations(sharp, 4):
        dis1 = (comb[0][0] - comb[1][0])**2 + (comb[0][1] - comb[1][1])**2
        dis2 = (comb[0][0] - comb[2][0])**2 + (comb[0][1] - comb[2][1])**2
        dis3 = (comb[0][0] - comb[3][0])**2 + (comb[0][1] - comb[3][1])**2
        dis4 = (comb[1][0] - comb[2][0])**2 + (comb[1][1] - comb[2][1])**2
        dis5 = (comb[1][0] - comb[3][0])**2 + (comb[1][1] - comb[3][1])**2
        dis6 = (comb[2][0] - comb[3][0])**2 + (comb[2][1] - comb[3][1])**2
        dis = [dis1, dis2, dis3, dis4, dis5, dis6]
        mindis = min(dis)
        side = 0
        diagonal = 0
        for i in range(6):
            if dis[i]==mindis:
                side += 1
            if dis[i]==2*mindis:
                diagonal += 1
        if side==4 and diagonal==2:
            ans += 1
    return ans

def main():
    S = []
    for _ in range(9):
        s = list(input())
        S.append(s)
    print(f(S))

if __name__=="__main__":
    main()
