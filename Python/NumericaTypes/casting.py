# In programming, casting refers to the process of converting one data type into another data type. This is sometimes necessary because different operations and functions may require different data types to work correctly.

# In Python, there are several built-in functions for casting data types, including:

# int(): converts a value to an integer
# float(): converts a value to a float
# str(): converts a value to a string
# For example, if you have a variable x that contains a string representation of an integer, you can cast it to an integer using the int() function:

x = "123"
y = int(x)
print(type(y))  # outputs "<class 'int'>"
# In the above code, we use the int() function to cast the string "123" to an integer. We store the result in a new variable y, and then print the type of y using the type() function. The output shows that y is an integer (<class 'int'>).

# Casting can also be used to convert values between different numeric types. For example, you can cast a float to an integer to truncate the decimal portion:

# python
# Copy code
x = 3.14
y = int(x)
print(y)  # outputs "3"
# In the above code, we cast the float 3.14 to an integer using the int() function. The result is the integer 3, which truncates the decimal portion of the float.
