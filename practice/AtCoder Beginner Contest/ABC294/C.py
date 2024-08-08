# Merge Sequences
def f(N, M, A, B):
    C = A + B
    C = sorted(C)
    C_dict = {}
    for i, v in enumerate(C):
        C_dict[v] = i
    A_ans = []
    B_ans = []
    for a in A:
        A_ans.append(C_dict[a]+1)
    for b in B:
        B_ans.append(C_dict[b]+1)
    return A_ans, B_ans

def main():
    N, M = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    A_ans, B_ans = f(N, M, A, B)
    print(*A_ans)
    print(*B_ans)

if __name__=="__main__":
    main()
