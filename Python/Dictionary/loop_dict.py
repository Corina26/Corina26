
student ={
    "course"     : "DevOps",
    "name"       : "John",
    "start_date" : "April",
    "end_date"   : "May"
}

# I would like to print all the keys in this dictionary. 

for k in student.keys():
    val = student.get(k)
    print("type of key is",type(k),f"and the key is {k} and value for the key is {val}")

# The usage of for loop above is not optimized. 

# items method

print(type(student.items()))
print(student.items())

for k,v in student.items():
    print(f"The key is {k}, the value is {v}")
