# Keys
def calc(N, M, K, CAR):
  ans = 0
  for bit in range(1 << N):
    nlist = [i+1 for i in list(range(N))]
    tmp = []
    for i in range(N):
      if bit & (1 << i):
        tmp.append(nlist[i])
    print(tmp)
    if len(tmp) != K:
      continue
    ans_flag = 0
    for car in CAR:
      for j in tmp:
        flag = True
        if j not in car[1:-1]:
          flag = False
          break
      if car[car[0]+1] == "o" and flag == False:
        ans_flag = 0
        break
      if car[car[0]+1] == "x" and flag == True:
        ans_flag = 0
        break
      ans_flag = 1
    if ans_flag == 1:
      ans += 1
  return ans

def main():
  N, M, K = [int(i) for i in input().split()]
  CAR = []
  for _ in range(M):
    car = list(input().split())
    r = list(car.pop(-1))
    ca = [int(i) for i in car]
    car = ca + r
    CAR.append(car)
  print(calc(N, M, K, CAR))

if __name__=="__main__":
  main()
