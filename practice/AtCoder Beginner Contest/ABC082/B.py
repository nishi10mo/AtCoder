def TwoAnagrams(s, t):
  s = sorted(s)
  t = sorted(t, reverse=True)
  if s < t:
    return "Yes"
  else:
    return "No"

s = input()
t = input()
print(TwoAnagrams(s, t))
