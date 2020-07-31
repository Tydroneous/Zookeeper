a = abs(int(input()))
b = abs(int(input()))
c = abs(int(input()))
class_a = 0
class_b = 0
class_c = 0

if a < 1000:
    if a % 2 == 1:
        class_a = (a // 2) + 1
    else:
        class_a = (a // 2)

if b < 1000:
    if b % 2 == 1:
        class_b = (b // 2) + 1
    else:
        class_b = (b // 2)

if c < 1000:
    if c % 2 == 1:
        class_c = (c // 2) + 1
    else:
        class_c = (c // 2)

total_desk = class_a + class_b + class_c
print(total_desk)
