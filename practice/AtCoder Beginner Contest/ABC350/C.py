# Sort

# 以下のコードはTLE
# def main():
#     n = int(input())
#     A = list(map(int, list(input().split())))
#     c = 0  # 何回交換したかを数える
#     rec = []  # 何番目と何番目を交換したかを記録
#     for i in range(n):
#         if A[i] != i+1:
#             p = A.index(i+1)
#             rec.append([i+1, p+1])
#             A[i], A[p] = A[p], A[i]
#             c += 1
#     print(c)
#     for i in range(c):
#         print(rec[i][0], rec[i][1])


def main():
    n = int(input())
    A = list(map(int, list(input().split())))
    c = 0  # 何回交換したかを数える
    rec = []  # 何番目と何番目を交換したかを記録


if __name__=="__main__":
    main()
