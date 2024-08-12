# Make Takahashi Happy
from itertools import permutations
def f(H, W, A):
    ans = 0
    direction = ["R"]*(H-1) + ["D"]*(W-1)
    unique_permutations = list(set(permutations(direction)))
    for perm in unique_permutations:
        happy = True
        history = set()
        h = 0
        w = 0
        history.add(A[h][w])
        for d in perm:
            if d=="R":
                w += 1
            else:
                h += 1
            if A[h][w] in history:
                happy = False
                break
            else:
                history.add(A[h][w])
        if happy == True:
            ans += 1
    return ans

def main():
    H, W = [int(i) for i in input().split()]
    A = []
    for _ in range(H):
        a = [int(i) for i in input().split()]
        A.append(a)
    print(f(H, W, A))

if __name__=="__main__":
    main()