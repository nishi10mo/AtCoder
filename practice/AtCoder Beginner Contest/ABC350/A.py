def main():
  S = list(input())
  S_ = [S[3], S[4], S[5]]
  num = int("".join(S_))
  if 0 < num < 350 and num != 316:
    print("Yes")
  else:
    print("No")

if __name__=="__main__":
  main()
