# Standing On The Shoulders

# 以下の解法はTLE
# def maxheight(N, AB):
#   rec = [0]*N
#   for i in range(N):
#     for j in range(N):
#       if j == i:
#         rec[i] += AB[j][1]
#       else:
#         rec[i] += AB[j][0]
#   return max(rec)    

def maxheight(N, AB):
  diff = []
  for i in range(N):
    diff_ = AB[i][1] - AB[i][0]
    diff.append(diff_)
  maxdiff = max(diff)
  base = 0
  for i in range(N):
    base += AB[i][0]
  ans = base + maxdiff
  return ans  

def main():
  N = int(input())
  AB = []
  for i in range(N):
    ab_ = [int(i) for i in input().split()]
    AB.append(ab_)
  print(maxheight(N, AB))

if __name__=="__main__":
  main()
