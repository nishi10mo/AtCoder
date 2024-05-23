# Piano
def calc(W, B):
  c = W + B
  piano = []
  for _ in range(16):
    piano += ["w", "b", "w", "b", "w", "w", "b", "w", "b", "w", "b", "w"]
  piano += ["w", "b", "w", "b", "w", "w", "b", "w"]
  for i in range(12):
    if i + c <=200:
      tmp = piano[i:i+c]
      W_ = tmp.count("w")
      B_ = tmp.count("b")
      if W_==W and B_==B:
        return "Yes"
  return "No"

def main():
  W, B = [int(i) for i in input().split()]
  print(calc(W, B))

if __name__=="__main__":
  main()
