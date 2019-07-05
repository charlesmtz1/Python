x = 0

while x < 10:
    print("Iteracion:" , x)
    if x == 5:
        break
    x += 1

x = 0

print("-------------------------------")

while x < 5:
    x += 1
    if x == 3:
        continue
    txt = "Iteracion: {}"
    print(txt.format(x))