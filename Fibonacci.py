def fibonacci(start_term, end_term, test_number):
    list_numbers = list()
    num1, num2 = 0, 1
    fibonacci = False

    while num1 < end_term:
        list_numbers.append(num1)
        num1, num2 = num2, num1 + num2

    print(list_numbers)
    
    if test_number < start_term or test_number > end_term:
        print("Invalid number")
    else:
        for element_list in list_numbers:
            if test_number == element_list:
                fibonacci = True
                break

    return fibonacci


start_term = int(input("Write start number: "))
end_term = int(input("Write end number: "))

test_number = int(input("Write test number: "))

if fibonacci(start_term, end_term, test_number) == True:
    print("Fibonacci number")
else:
    print("Is not a Fibonacci number")