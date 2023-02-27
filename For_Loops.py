
countries = ["Denmark", "Sweden", "Norway", "Finland", "Iceland", "Faroe Islands", "Greenland"]
for x in countries:
    print(x)

countries = ["Denmark", "Sweden", "Norway", "Finland", "Iceland", "Faroe Islands", "Greenland"]
for x in countries:
    print(x)
    if x == "Iceland":
        break

countries = ["Denmark", "Sweden", "Norway", "Finland", "Iceland", "Faroe Islands", "Greenland"]
for x in countries:
    if x == "Norway":
        continue
    print(x)


for x in range (2, 6):
    print(x)


for x in range(7):
    print(x)
else:
    print("Done")
