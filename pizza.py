size = input('What size pizza? ')
toppings = int(input('How many toppings? (1-4) '))

toppings = -1
while toppings < 0 and toppings > 5:
    try:
        toppings = int(input('How many toppings? (1-4) '))
    except:
        pass
    