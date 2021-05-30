import sys

data = sys.stdin.readlines()
d = {}
for i in data:
    a = i[:i.index(' - ')].strip()
    b = i[i.index(' - ') + 2:].strip()
    if b not in d:
        d[b] = a
    elif b not in d[a]:
        d[b] += '; ' + a

for key, value in d.items():
    print(key + ":", value)
