#Exercise 4
#Do the next exercise using if/else statements
#Price of a house $1M
#If buyer has good credit
#   they need to put down 10%
#Otherwise
#   they need to put down 20%
#Print the down payment

price_house = 1000000
good_credit = False
txt = "The buyer needs to pay: ${}"

if good_credit == True:
    payment = price_house * 0.10
else:
    payment = price_house * 0.20

print(txt.format(payment))