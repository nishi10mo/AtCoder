def Daydream(s):
  def checkDream(s):
    if len(s)>=5 and s[-5]=="d" and s[-4]=="r" and s[-3]=="e" and s[-2]=="a" and s[-1]=="m":
      del s[-5:]
      return s
  def checkDreamer(s):
    if len(s)>=7 and s[-7]=="d" and s[-6]=="r" and s[-5]=="e" and s[-4]=="a" and s[-3]=="m" and s[-2]=="e" and s[-1]=="r":
      del s[-7:]
      return s
  def checkerase(s):
    if len(s)>=5 and s[-5]=="e" and s[-4]=="r" and s[-3]=="a" and s[-2]=="s" and s[-1]=="e":
      del s[-5:]
      return s
  def checkeraser(s):
    if len(s)>=6 and s[-6]=="e" and s[-5]=="r" and s[-4]=="a" and s[-3]=="s" and s[-2]=="e" and s[-1]=="r":
      del s[-6:]
      return s
  flag = True
  while flag:
    l = len(s)
    if l == 0:
      return "YES"
    checkDream(s)
    checkDreamer(s)
    checkerase(s)
    checkeraser(s)
    l_ = len(s)
    if l == l_:
      flag = False
  return "NO"

s = list(input())
print(Daydream(s))
