def calculate_coins(amount):
    total_cents = int(amount * 100)

    quarters = total_cents // 25
    total_cents = total_cents % 25

    dimes = total_cents // 10
    total_cents = total_cents % 10

    nickels = total_cents // 5
    total_cents = total_cents % 5

    pennies = total_cents

    return quarters, dimes, nickels, pennies

amount = float(input("Enter the dollar amount: "))
quarters, dimes, nickels, pennies = calculate_coins(amount)

print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)
