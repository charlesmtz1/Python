#No usar "x" * 5

numbers = [5, 2, 5, 2, 5]
character = 'x'

for number in numbers:
    for symbol in range(number):
        print(f"{character}", end="")
    print("")
