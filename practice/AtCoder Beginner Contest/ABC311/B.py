# Vacation Together
def f(N, D, S):
    calender = [[] for _ in range(D)]
    for i in range(N):
        for j in range(D):
            calender[j].append(S[i][j])
    ans = 0
    c = 0
    for days in calender:
        flag = True
        for day in days:
            if day == "x":
                flag = False
                break
        if not flag:
            c = 0
            continue
        c += 1
        ans = max(ans, c)
    return ans

def main():
    N, D = [int(i) for i in input().split()]
    S = []
    for _ in range(N):
        s = list(input())
        S.append(s)
    print(f(N, D, S))

if __name__=="__main__":
    main()
