
comando = True
car_on = False

while comando:
    comando = input(">").lower()

    if comando == "start":
        if not car_on:
            car_on = True
            print("\nYou started the car!\n")
        else:
            print("\nThe car is already on!!\n")
        continue

    if comando == "stop":
        if car_on:
            car_on = False
            print("\nYou stopped the car!\n")
        else:
            print("\nYou can't stop the car, because it's off!!\n")
        continue

    if comando == "help":
        print("\nStart -> to start the car")
        print("Stop -> to stop the car")
        print("Quit -> to exit the program\n")
        continue

    if comando == "quit":
        print("\nGoodbye!")
        break

    print("\nOpcion no valida!!\n")
    