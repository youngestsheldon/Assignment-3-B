size = ""
while size != "large" and size != "extra large":
    size = input('What size pizza? ').lower()
toppings = int(input('How many toppings? (1-4) '))

toppings = -1
while toppings < 0 and toppings > 5:
    try:
        toppings = int(input('How many toppings? (1-4) '))
    except:
        pass

cost = 0
if size == "large":
    cost += 6
else:
    cost += 10

if toppings == 1:
    cost += 1
elif toppings == 2:
    cost += 1.75
elif toppings == 3:
    cost += 2.50
elif toppings == 4:
    cost += 3.35


print(f"\nYour subtotal comes to: ${round(cost, 2)}, tax: {round(cost*0.13,2)}, and total: $")

