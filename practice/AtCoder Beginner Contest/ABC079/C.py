def TrainTicket(a, b, c, d):
    ch = ["+", "-"]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                if eval(a + ch[i] + b + ch[j] + c + ch[k] + d)==7:
                    return a + ch[i] + b + ch[j] + c + ch[k] + d + "=7"

a, b, c, d = list(input())
print(TrainTicket(a, b, c, d))
