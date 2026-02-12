import sys
data = sys.stdin.read().split()
it = iter(data)
def printyn(isok):
    print("Yes" if isok else "No")

q = int(next(it))
vol = 0
is_music = False
for _ in range(q):
    match next(it):
        case "1":
            vol += 1
        case "2":
            vol = max(0, vol - 1)
        case "3":
            is_music = not is_music
        case _:
            continue
    printyn(vol >= 3 and is_music)
