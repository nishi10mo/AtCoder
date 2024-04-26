def AllGreen(d, g, info):
    if d == 0:
        return 0
    n = min(g//(100*d), info[d][0])
    score = 0
    for i in range(d-1, -1, -1):
        for j in range(info[i][1]):
            score += 100*(i+1)
            c += 1
            if j == info[i][1]-1:
                score += info[i][2]
            if score >= g:
                return c

d, g = map(int, list(input().split()))
info = []
for i in range(d):
    tmp = list(map(int, list(input().split())))
    info.append(tmp)
print(AllGreen(d, g, info))
