n = int(input())
r = int(input())
count = 0
while True:
    if n > r:
        n = (n // 2)
        count += 1
    else:
        break

print(count * 12)
