# Frequency
from collections import defaultdict
def f(S):
    count = defaultdict(int)
    for s in S:
        count[s] += 1
    count = dict(count)
    count = dict(sorted(count.items(), key=lambda x:x[1], reverse=True))
    max_c = max(count.values())
    cand = []
    for key, val in count.items():
        if val == max_c:
            cand.append(key)
        else:
            break
    cand = sorted(cand)
    return cand[0]

def main():
    S = list(input())
    print(f(S))

if __name__=="__main__":
    main()
