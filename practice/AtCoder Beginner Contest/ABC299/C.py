# Dango
def f(N, S):
  i = 0
  ans = -1
  while i < N:
    level = 0
    if S[i]=="o":
      level += 1
      j = i+1
    elif S[i]=="-" and S[i+1]=="o":
      level += 1
      j = i+2
    else:
      level = -1
      j = i+1
    while S[j]=="o":
      level += 1
      j += 1
    i = j
    ans = max(ans, level)

def f(N, S):
  i = 0
  ans = -1
  while i < N:
    if S[i]=="o" and S[i+1]=="o":

      level += 1
      j = i+1
    elif S[i]=="-" and S[i+1]=="o":
      level += 1
      j = i+2
    else:
      level = -1
      j = i+1
    while S[j]=="o":
      level += 1
      j += 1
    i = j
    ans = max(ans, level)


def main():
  N = int(input())
  S = list(input())
