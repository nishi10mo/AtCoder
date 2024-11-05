# 3.14
def f(N):
    pi = list("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")
    ans = pi[:N+2]
    return "".join(ans)

def main():
    N = int(input())
    print(f(N))

if __name__=="__main__":
    main()
