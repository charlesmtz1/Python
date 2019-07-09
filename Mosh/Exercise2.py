#Exercise 2
#Ask two questions: person's name and favourite color. Then, print a message like "Mosh likes blue. 

name = input("What is your name?: ")
color = input("and your favourite color?: ")
txt = "Hi {}, {} is a nice color!"

print(txt.format(name,color))
