# Manga
def f(N, books):
    books = sorted(books)
    s = [books[0]]
    l = []
    for i in range(1, N):
        if books[i] == s[-1]:
            l.append(books[i])
        else:
            s.append(books[i])
    s += l   
    idx = 0
    ans = 0
    while idx < len(s):
        if s[idx] == ans+1:
            idx += 1
        else:
            if len(s) - idx < 2:
                break
            s.pop()
            s.pop()
        ans += 1
    return ans        

def main():
    N = int(input())
    books = [int(i) for i in input().split()]
    print(f(N, books))

if __name__=="__main__":
    main()
