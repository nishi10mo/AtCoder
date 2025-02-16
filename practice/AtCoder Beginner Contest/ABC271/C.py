# Manga
def f(N, books):
    books = sorted(books)
    ans = 0
    if books[0] == 1:
        ans += 1
    if len(books) == 1:
        return ans
    left = 0
    right = N-1
    if books[left] != 1:
        if right > left + 1:
            right -= 2
            ans += 1
            books[left] += 1
        else:
            return ans
    while left < right:
        if books[left+1] == books[left] + 1:
            ans += 1
            left += 1
        else:
            if right > left + 1:
                right -= 2
                ans += 1
                books[left] += 1
            else:
                break
    return ans

def main():
    N = int(input())
    books = [int(i) for i in input().split()]
    print(f(N, books))

if __name__=="__main__":
    main()
