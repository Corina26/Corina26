# Create a method that takes one dict and one value as parameter.
# check if the given value exist in the dictionary.
# If the given value exist in dictionary return True, return False.
# do both for key and value. 

def is_value_present(dictionary,value):
    # How can I check if the value is present in the dict object?
    # How can you find all values in dictionary object? 
    # values()
    return value in dictionary.values()

def is_key_present(dictionary,key):
    # I would get all the keys in dictionary and check if the key is one of them.
    return key in dictionary.keys()

student ={
    'name':'y',
    'last_name':'t',
    'school_num':390
}

print(is_value_present(student,390)) # True
print(is_key_present(student,390)) # False

