import sys
from math import ceil

input = sys.stdin.readline


D, G = map(int, input().rstrip().split())

Ps = [0] * D
Cs = [0] * D
for i in range(D):
    p, c = map(int, input().rstrip().split())
    Ps[i] = p
    Cs[i] = c

min_num = sum(Ps)
for i in range(1 << D):
    score = 0
    num = 0
    largest_idx = 0
    for j in range(D):
        if (i >> j) & 1:
            score += 100 * (j + 1) * Ps[j] + Cs[j]
            num += Ps[j]
        else:
            largest_idx = j
    if score < G:
        margin_num = ceil((G - score) / ((largest_idx + 1) * 100))
    else:
        margin_num = 0
    if margin_num < Ps[largest_idx] and num + margin_num < min_num:
        min_num = num + margin_num
print(min_num)
