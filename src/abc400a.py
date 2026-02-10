import sys
it = sys.stdin.readline()

a = int(it)
print(400 // a if 400 % a == 0 else -1)
