# Chinese Restaurant
def f(N, p):
    ans = 0
    diffs = []
    for i, v in enumerate(p):
        diff = abs(v-i)
        diffs.append(diff)
    for _ in range(N):
        total = sum(diffs)
        diffs = [i-1 for i in diffs]
    total = sum(diffs)

        
        

def main():
    N = int(input())
    p = [int(i) for i in input().split()]
