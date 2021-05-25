import sys
 
d = {}
data = list(map(str.strip, sys.stdin))
for i in data:
    a, b = i.split('-')
    a = a.strip()
    b = b.strip()
    if b not in d:
        d[b] = a
    elif a not in d[b]:
        d[b] += ', ' + a

for key, value in d.items() :
    print (key,": ", value)
