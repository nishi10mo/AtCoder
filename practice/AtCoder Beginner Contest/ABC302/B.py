# Find snuke
def f(H, W, S):
    def fivecheck(x, y):
        target1 = ["s", "n", "u", "k", "e"]
        target2 = ["e", "k", "u", "n", "s"]
        for i in range(5):
            if S[x+i][y:y+5] == target1:
                return [[x+i, y], [x+i, y+1], [x+i, y+2], [x+i, y+3], [x+i, y+4]]
            elif S[x+i][y:y+5] == target2:
                return [[x+i, y+4], [x+i, y+3], [x+i, y+2], [x+i, y+1], [x+i, y]]
        for i in range(5):
            column = []
            for j in range(5):
                column.append(S[x+j][y+i])
            if column == target1:
                return [[x, y+i], [x+1, y+i], [x+2, y+i], [x+3, y+i], [x+4, y+i]]
            elif column == target2:
                return [[x+4, y+i], [x+3, y+i], [x+2, y+i], [x+1, y+i], [x, y+i]]
        cross = []
        for i in range(5):
            cross.append(S[x+i][y+i])
        if cross == target1:
            return [[x, y], [x+1, y+1], [x+2, y+2], [x+3, y+3], [x+4, y+4]]
        elif cross == target2:
            return [[x+4, y+4], [x+3, y+3], [x+2, y+2], [x+1, y+1], [x, y]]
        cross = []
        for i in range(5):
            cross.append(S[x+i][y+4-i])
        if cross == target1:
            return [[x, y+4], [x+1, y+3], [x+2, y+2], [x+3, y+1], [x+4, y]]
        elif cross == target2:
            return [[x+4, y], [x+3, y+1], [x+2, y+2], [x+1, y+3], [x, y+4]]
        return False
    for i in range(H-4):
        for j in range(W-4):
            results = fivecheck(i, j)
            if results != False:
                return results

def main():
    H, W = [int(i) for i in input().split()]
    S = []
    for _ in range(H):
        s = list(input())
        S.append(s)
    results = f(H, W, S)
    for ans in results:
        ans = [i+1 for i in ans]
        print(*ans)

if __name__=="__main__":
    main()
