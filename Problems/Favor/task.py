k = int(input())
count = 0
total = 0
while count <= k:
    total += count
    count += 1

print(total)
# alt (k * (k + 1)) // 2
