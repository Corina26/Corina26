# In the factory we need to create a program that can 
# find if we can do the shipment and, if we can do the shipment
# it will tell us how many small package we should ship.
# First we need to get total kilogram of the shipment,
# to reach this total kilogram of shipment we can use small and big packages. 
# Every big package is 5 kilogram and every small packages is 1 kilogram.
# We have limited amount of small and big packages. 
# Ask user how many big and how many small package  they have.
# Ask user what is the total goal kilogram of the shipment.
# Print whether they can ship, if they can ship print how many small packages they need. 
# Assume big packages is used before small packages. 


number_of_big = int(input("Enter the number of big packages you have: "))
number_of_small = int(input("Enter the number of small packages you have: "))
goal_shipment = int(input("Enter the EXACT amount of KG that needs to be shipped. -> "))

# First we should definitely start using big packages
# I have to find big package I need for this shipment

big_package_needed = goal_shipment // 5

if number_of_big >= big_package_needed:
    # WE should find the part that we cannot complete it with the bigpackages.
    small_package_needed = goal_shipment%5
    if number_of_small >= small_package_needed:
        print(f"We can do this shipment using {small_package_needed} small packages.")
    else:
        print("This shipment can't be done")

elif big_package_needed>number_of_big:
    amount_with_big = number_of_big * 5
    small_package_needed = goal_shipment - amount_with_big
    if number_of_small>=small_package_needed:
        print(f"I can do this shipment using {small_package_needed} small packages.")
    else:
        print("This shipment can't be done")
