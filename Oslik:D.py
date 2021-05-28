n = int(input())
while True:
    str = input()
    if len(str) == 0:
        break
    if str[0].isupper():
        if str[-1] == '?':
            n = n - 5
        elif (str[-1] == '.') or (str[-1] == '!'):
            n = n - 3
if n < 0:
    n = 0
print(n)
