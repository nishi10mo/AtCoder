# False Hope
from itertools import permutations
def f(c):
    bottom = 1
    for i in range(2, 10):
        bottom *= i
    top = bottom
    for v in permutations(c):
        for i in range(7):
            if v[i]==v[i+1] and v[i+1]!=v[i+2]:
                top -= 1
                break
    print("top", top)
    print("bottom", bottom)
    return top/bottom

def main():
    c = []
    for _ in range(3):
        c1, c2, c3 = [int(i) for i in input().split()]
        c.append(c1)
        c.append(c2)
        c.append(c3)
    print(f(c))

if __name__=="__main__":
    main()
