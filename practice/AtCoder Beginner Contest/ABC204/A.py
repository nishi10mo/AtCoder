# Rock-paper-scissors
def decideChoise(a):
    choices = [0, 1, 2]
    if a[0] == a[1]:
        return a[0]
    else:
        if 0 not in a:
            return 0
        elif 1 not in a:
            return 1
        else:
            return 2

def main():
    a = [int(i) for i in input().split()]
    print(decideChoise(a))

if __name__=="__main__":
    main()


