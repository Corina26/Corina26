
number = int(input("12345 "))

# Reverse the digits of the number
reverse_number = 0
while number > 0:
    # Get the last digit of the number
    last_digit = number % 10
    # Add the last digit to the reverse_number
    reverse_number = (reverse_number * 10) + last_digit
    # Remove the last digit from the number
    number //= 10

# Print the reversed number
print("The reversed number is:", reverse_number)



