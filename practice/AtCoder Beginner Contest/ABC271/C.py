# Manga
def f(N, books):
    books = set(books)
    dup = N - len(books)
    books = list(books)
    pre = 0
    while books:
        a = books[0]
        if a == pre+1:
            pre = books.pop(0)
        else:
            if dup > 1:
                dup -= 2
                pre += 1
            elif len(books) > 2:
                final = books.pop(-1)
                semifinal = books.pop(-1)
                pre += 1
            else:
                break
    if dup > 1:
        pre += dup//2
    return pre  

def main():
    N = int(input())
    books = [int(i) for i in input().split()]
    print(f(N, books))

if __name__=="__main__":
    main()
