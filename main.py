MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

bank = 0.0

is_on = True


def collect(cost, user_input):
    count = 0
    payment_value = 0.0
    collecting = True

    while collecting:
        count += 1

        quarters = input('Quarters: ')
        payment_value += float(quarters) * 0.25
        if payment_value >= cost:
            break

        dimes = input('Dimes: ')
        payment_value += float(dimes) * 0.10
        if payment_value >= cost:
            break

        nickles = input('Nickles: ')
        payment_value += float(nickles) * 0.05
        if payment_value >= cost:
            break

        pennies = input('Pennies: ')
        payment_value += float(pennies) * 0.01

        if count > 2:
            collecting = False

        if payment_value < cost and count < 3:
            print('Your current balance is $' + str(payment_value) + ' Please add more money, the item costs $' + str(
                cost))

    result = calc_and_resource_manager(cost, payment_value, user_input)
    return result


def resource_checker(user_input):
    for (k, v), (k2, v2) in zip(resources.items(), MENU[user_input]['ingredients'].items()):
        # print(f"From resources {k} : {v}, from ingredients {k2} : {v2}")
        if v < v2:
            print('Sorry there is not enough ' + k)
            return False
    return True


def calc_and_resource_manager(cost, payment_value, user_input):
    global bank
    if payment_value >= cost:
        change = payment_value - cost
        bank += cost
        for item in MENU[user_input]['ingredients']:
            resources[item] -= MENU[user_input]['ingredients'][item]
        data = {
            "isServed": True,
            "funds": round(change, 2)
        }
        return data
    else:
        data = {
            "isServed": False,
            "funds": round(payment_value, 2)
        }
        return data


def order(user_input):
    if resource_checker(user_input):
        response = collect(MENU[user_input]["cost"], user_input)
        if response["isServed"]:
            if response["funds"] > 0.0:
                print(f'Thanks for your {user_input} order ☕️, here is your change: ${str(response["funds"])} 🪙')
            else:
                print(f'Thanks for your {user_input} order ☕️. Enjoy!')
        else:
            print(f'Sorry, that is not enough money. Refunded ${str(response["funds"])}.')


def report():
    print('Water: ' + str(resources['water']) + 'ml')
    print('Milk: ' + str(resources['milk']) + 'ml')
    print('Coffee: ' + str(resources['coffee']) + 'g')
    print('Money: $' + str(bank))


while is_on:
    userInput = input('What would you like? (espresso / latte / cappuccino): ').strip()

    if userInput == 'espresso':
        order(userInput)
    elif userInput == 'latte':
        order(userInput)
    elif userInput == 'cappuccino':
        order(userInput)
    elif userInput == 'report':
        report()
    elif userInput == 'off':
        is_on = False
    else:
        userInput = input('What would you like? (espresso / latte / cappuccino): ').strip()

print('Power off.')
