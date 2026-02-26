s = input()
t = ""
is_ok = False
for c in s:
  if c == '#':
    t += '#'
    is_ok = False
  else:
    if not is_ok:
      t += 'o'
      is_ok = True
    else:
      t += '.'
print(t)
