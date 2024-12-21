# Equally
def f(A, B, C):
    if A == B == C:
        return "Yes"
    if A + B == C or B + C == A or C + A == B:
        return "Yes"
    return "No"

def main():
    A, B, C = [int(i) for i in input().split()]
    print(f(A, B, C))

if __name__ == '__main__':
    main()
