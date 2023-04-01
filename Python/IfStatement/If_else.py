# If the given grade for student is A print 
# "that's an excellent grade." 
# If the given grade for students is B print 
# "That's a good grade."
# IN all other grades just print 
# "Your grade should be improved."

# Only one of the above conditon can be true 
# that's why best practice would be comnbining all in one if-else statement

grade = input("Please enter your grade letter: -> ").upper()
# We used .upper method after the input because in our if statement 
# we are expecting grade text to be given in an uppercase letter. 
# any input will be converted to upper case so that our code can work in both situation. 


if grade == 'A':
    print("That's an excellent grade.")
elif grade == "B":
    print("That's a good grade.")
else:
    # When the grade is not A nor is B, then this else statement gets executed. 
    print("Your grade should be improved.")

# Python way of saying in 'all other conditions' is using else statement. 
# Else statement gets executed when all previous conditons are False. 
