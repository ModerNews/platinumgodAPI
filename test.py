slots = 40
wagony_p = 40
wagony_k = 22

passangers = 0

dict = {}
for i in range(1, wagony_p + 1):
    dict[i] = i
    passangers += i

pusty_wagon = wagony_p - 1
while len(dict.items()) > wagony_k:
    for j in range(dict[i]):
        if dict[pusty_wagon] < slots:
            dict[pusty_wagon] += 1
        else:
            pusty_wagon -= 1
            dict[pusty_wagon] += 1
    dict.pop(i)
    i -= 1

print(dict)
print(dict[2])
print(passangers)