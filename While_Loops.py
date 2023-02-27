
i = 0
while i < 10:
    print("Hello")
    i += 1

i = 0
while i < 10:
    print(i)
    if i == 6:
        break
    i += 1

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

i = 1
while i < 10:
    print(i)
    i += 1
else:
    print("Done")
