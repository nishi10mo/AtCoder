def AllGreen(d, g, info):
    if d == 0:
        return 1e9
    n = min(g//(100*d), info[d-1][0])
    s = 100*d*n
    if n==info[d-1][0]:
        s += info[d-1][1]
    if s < g:
        n += AllGreen(d-1, g-s, info)
    return min(n, AllGreen(d-1, g, info))

d, g = map(int, list(input().split()))
info = []
for i in range(d):
    tmp = list(map(int, list(input().split())))
    info.append(tmp)
print(AllGreen(d, g, info))
