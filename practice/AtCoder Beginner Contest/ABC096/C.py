# def GridRepainting2(h, w, s):
#   for i in range(h):
#     for j in range(w):
#       if s[i][j]==".":
#         continue
#       else:
#         if i==0 and j==0 and s[i][j+1]=="." and s[i+1][j]==".":
#           return "No"
#         if i==0 and 0<j<w-1 and s[i][j-1]=="." and s[i][j+1]=="." and s[i+1][j]==".":
#           return "No"
#         if i==0 and j==w-1 and s[i][j-1]=="." and s[i+1][j]==".":
#           return "No"
#         if 0<i<h-1 and j==0 and s[i-1][j]=="." and s[i][j+1]=="." and s[i+1][j]==".":
#           return "No"
#         if i==h-1 and j==0 and s[i-1][j]=="." and s[i][j+1]==".":
#           return "No"
#         if i==h-1 and 0<j<w-1 and s[i][j-1]=="." and s[i-1][j]=="." and s[i][j+1]==".":
#           return "No"
#         if i==h-1 and j==w-1 and s[i][j-1]=="." and s[i-1][j]==".":
#           return "No"
#         if 0<i<h-1 and j==w-1 and s[i-1][j]=="." and s[i][j-1]=="." and s[i+1][j]==".":
#           return "No"
#         if 0<i<h-1 and 0<j<w-1 and s[i][j-1]=="." and s[i-1][j]=="." and s[i][j+1]=="." and s[i+1][j]==".":
#           return "No"
#   return "Yes"

def GridRepainting2(h, w, s):
  for i in range(h):
    for j in range(w):
      if s[i][j]==".":
        continue
      else:
        flag=0
        for x, y in [[0,1], [0,-1], [-1,0], [1,0]]:
          if 0<=i+x<=h-1 and 0<=j+y<=w-1 and s[i+x][j+y]=="#":
            flag=1
        if flag==0:
          return "No"
  return "Yes"


h, w = list(map(int, list(input().split())))
s = []
for i in range(h):
  s_ = list(input())
  s.append(s_)
print(GridRepainting2(h, w, s))
