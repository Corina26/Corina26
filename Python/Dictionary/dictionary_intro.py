# To be able to create a dictionary object we could use 
# dict() function or we could use curly braces. 
# creating empty dictionary

d1 = dict()
d2 = {}
print(type(d1)) # <class 'dict'>
print(type(d2)) # <class 'dict'>

# let's create one dictonary
#NOTE: Key and value in dictionary objects are separated by column, 
# and key-value PAIRS are separated by comma.
laptop ={
    "brand" : "Apple",
    "model" : "Macbook Pro",
    "year"  : "2021"}
print(len(laptop))

# How do you think we could access the elements? 
# dictionary objects don't use indexing. 
# using keys in the dictionary object, I could retrive associated values.

print(laptop["brand"])

# also get() method could be used for retrieving the values from map objects. 

print(laptop.get('brand'))

# The difference between using get method or square brackets is when key is not present
# square brackets will generate an error. In the get method we wouldn't encounter this error.

print(laptop.get("storage")) # -> value None