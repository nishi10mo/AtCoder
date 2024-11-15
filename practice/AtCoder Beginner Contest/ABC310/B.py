# Strictly Superior
def f(N, M, PCF):
    for i in range(N):
        price = PCF[i][0]
        count = PCF[i][1]
        for j in range(N):
            flag = True
            for k in range(count):
                if not (PCF[i][k+2] in PCF[j][2:2+PCF[j][1]]):
                    flag = False
                    break
            if price < PCF[j][0]:
                flag = False
            if price == PCF[j][0] and PCF[i][2:2+PCF[i][1]] == PCF[j][2:2+PCF[j][1]]:
                flag = False
            if not flag:
                continue
            return "Yes"
    return "No"

def main():
    N, M = [int(i) for i in input().split()]
    PCF = []
    for _ in range(N):
        pcf = [int(i) for i in input().split()]
        PCF.append(pcf)
    print(f(N, M, PCF))

if __name__=="__main__":
    main()
