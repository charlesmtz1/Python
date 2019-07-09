#Exercise 3
#Ask a user their weight (in pounds), convert it to kilograms and print on the terminal.

weight = input("What is your weight(lbs)?: ")
kgs = int(weight) * 0.453592

txt = "Your weight in kgs is: {}"

print(txt.format(kgs))
