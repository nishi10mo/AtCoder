# Substring
# def mCn(m, n):
#     # m,nはint
#     # m > nを想定
#     # 出力ansはint
#     top = 1
#     bottom = 1
#     for i in range(m, m-n, -1):
#         top *= i
#     for i in range(n, 0, -1):
#         bottom *= i
#     print("top")
#     print(top)
#     print("bottom")
#     print(bottom)
#     ans = top//bottom
#     print("ans")
#     print(ans)
#     return ans

# def calc(S):
#     # Sは文字列
#     # 出力ansはint
#     m = len(S)
#     ans = 0
#     for n in range(1, m+1):
#         ans += mCn(m, n)
#     return ans

def calc(S):
    # Sは文字列
    # 出力ansはリスト
    S = list(S)
    n = len(S)
    ans = []
    for i in range(n):
        for j in range(n-i):
            tmp = S[i:i+j+1]
            tmp = "".join(tmp)
            if tmp in ans:
                continue
            ans.append(tmp)
    return len(ans)

def main():
    S = input()
    print(calc(S))

if __name__=="__main__":
    main()
