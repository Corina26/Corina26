
# since the dictionary objects are mutable, 
# we could change elements of dictionary individually.

student = {
    "course" : "cyber security",
    'city'   : 'Chicago',
    'age'    : 29,
}

# this particular student changed interest and wants to join in DevOps course. 

student["course"] = 'DevOps'
print(student.get("course"))

# THe line below will add a new key-value pair in to dictionary object. 
student['key1'] = "Dev Ops"

print(student)


# How to remove elements from dictionary object. 


# del keyword
# THe line below will add remove key-value pair in dictionary object. 
del student['city']
print(student)
#NOTE: When del keyword is used with key that is not present in a dictionary object 
# it will generate Key Error. 