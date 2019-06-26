
lista = list(("Rei", "Dia", "Mizuki"))

for x in lista:
    print(x)

print("---------------------")

for x in "Kurosawa":
    print(x)
    if x == 's':
        break

print("---------------------")

for x in "Intel":
    if x == 't':
        continue
    print(x)

