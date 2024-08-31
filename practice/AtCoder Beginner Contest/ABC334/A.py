# Christmas Present
def f(B, G):
    if B > G:
        return "Bat"
    else:
        return "Glove"

def main():
    B, G = [int(i) for i in input().split()]
    print(f(B, G))

if __name__=="__main__":
    main()
