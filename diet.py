import sys

data = []
while True:
    x = input()
    if (x.find('-') == -1):
        break
    data.append(x)
d = {}
for i in data:
    a = i[:i.index(' - ')].strip()
    b = i[i.index(' - ') + 2:].strip()
    if b not in d:
        d[b] = a
    elif a not in d[b]:
        d[b] += ', ' + a

for key, value in d.items():
    print(key, ": ", value)
