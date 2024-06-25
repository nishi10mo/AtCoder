# Count xxx
def f(N, S):
  l = 0
  mx = [0]*26
  while l < N:
    r = l + 1
    while r < N and S[l] == S[r]:
      r += 1
    c = ord(S[l]) - ord("a")
    mx[c] = max(mx[c], r-l)
    l = r
  
  ans = sum(mx)
  return ans

def main():
  N = int(input())
  S = list(input())
  print(f(N, S))

if __name__=="__main__":
  main()