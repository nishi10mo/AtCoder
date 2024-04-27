# def GridAndMagnet(i, j, h, w, s):
#   if s[i][j]=="#":
#     return 0
#   if i==0 and j==0:
#     if s[i][j+1]=="#" or s[i+1][j]=="#":
#       return 1
#     return 1 + GridAndMagnet(i, j+1, h, w, s) + GridAndMagnet(i+1, j, h, w, s)
#   if i==0 and j==w-1:
#     if s[i][j-1]=="#" or s[i+1][j]=="#":
#       return 1
#     return 1 + GridAndMagnet(i, j-1, h, w, s) + GridAndMagnet(i+1, j, h, w, s)
#   if i==h-1 and j==0:
#     if s[i-1][j]=="#" or s[i][j+1]=="#":
#       return 1
#     return 1 + GridAndMagnet(i-1, j, h, w, s) + GridAndMagnet(i, j+1, h, w, s)
#   if i==h-1 and j==w-1:
#     if s[i-1][j]=="#" or s[i][j-1]=="#":
#       return 1
#     return 1 + GridAndMagnet(i-1, j ,h, w, s) + GridAndMagnet(i, j-1, h, w, s)
#   if i==0 and 0<j<w-1:
#     if s[i][j-1]=="#" or s[i][j+1]=="#" or s[i+1][j]=="#":
#       return 1
#     return 1 + GridAndMagnet(i, j-1, h, w, s) + GridAndMagnet(i, j+1, h, w, s) + GridAndMagnet(i+1, j, h, w, s)
#   if 0<i<h-1 and j==0:
#     if s[i-1][j]=="#" or s[i][j+1]=="#" or s[i+1][j]=="#":
#       return 1
#     return 1 + GridAndMagnet(i-1, j, h, w, s) + GridAndMagnet(i, j+1, h, w, s) + GridAndMagnet(i+1, j, h, w, s)
#   if i==h-1 and 0<j<w-1:
#     if s[i][j-1]=="#" or s[i-1][j]=="#" or s[i][j+1]=="#":
#       return 1
#     return 1 + GridAndMagnet(i, j-1, h, w, s) + GridAndMagnet(i-1, j, h, w, s) + GridAndMagnet(i, j+1, h, w, s)
#   if 0<i<h-1 and j==w-1:
#     if s[i-1][j]=="#" or s[i][j-1]=="#" or s[i+1][j]=="#":
#       return 1
#     return 1 + GridAndMagnet(i-1, j, h, w, s) + GridAndMagnet(i, j-1, h, w, s) + GridAndMagnet(i+1, j, h, w, s)
#   if 0<i<h-1 and 0<j<w-1:
#     if s[i-1][j]=="#" or s[i+1][j]=="#" or s[i][j-1]=="#" or s[i][j+1]=="#":
#       return 1
#     return 1 + GridAndMagnet(i-1, j ,h ,w, s) + GridAndMagnet(i+1, j, h, w, s) + GridAndMagnet(i, j-1, h, w, s) + GridAndMagnet(i, j+1, h, w, s)

# h, w = list(map(int, list(input().split())))
# s = []
# for i in range(h):
#   s_ = list(input())
#   s.append(s_)
# record = [[0]*w for i in range(h)]
# for i in range(h):
#   for j in range(w):
#     record[i][j] = GridAndMagnet(i, j, h, w, s)
# print(max(record))

