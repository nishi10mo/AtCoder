# Sort
def main():
    n = int(input())
    A = [int(i)-1 for i in input().split()]
    index = [0]*n  # 特定の数字がAのどこにあるかを記録
    for i in range(n):
        index[A[i]] = i
    c = 0  # 何回交換したかを数える
    rec = []  # 何番目と何番目を交換したかを記録
    for i in range(n):
        if A[i] != i:
            rec.append([i+1, index[i]+1])
            A[i], A[index[i]] = A[index[i]], A[i]
            index[A[index[i]]], index[i] = index[i], index[A[index[i]]]
            c += 1
    print(c)
    for i in range(c):
        print(rec[i][0], rec[i][1])

if __name__=="__main__":
    main()
