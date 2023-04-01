
# Class is on the line below.
class Employee:
    def __init__(self,name,last_name,role):
        self.full_name = name +" "+ last_name + role
        self.role = role

# I have a class that doesn't have any attribute or any method. 

# I can create a instance of a class, which gets all attributes and methods of class.
employee1 = Employee("Daniel","White","Software Developer")
employee2 = Employee("Amy","Trinity","DevOps")
# In the line below we will see where the object is located,
# however, we could alter what we see when we print the object itself. 
print(employee1)
print(employee1.full_name, "and the role of employee1 instance is",employee1.role)
print(employee2.role)