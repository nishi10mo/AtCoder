# Sierpinski carpet
def output(N):
  if N == 0:
    ans = [["#"]]
    return ans
  ans = []
  pre = output(N-1)
  for i in pre:
    tmp = i*3
    ans.append(tmp)
  for i in pre:
    center = ["."]*(3**(N-1))
    tmp = i + center + i
    ans.append(tmp)
  for i in pre:
    tmp = i*3
    ans.append(tmp)
  return ans

def main():
  N = int(input())
  ans = output(N)
  for i in ans:
    print("".join(i))

if __name__=="__main__":
  main()
