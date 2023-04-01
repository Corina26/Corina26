#Functions that we can use with lists and list function
# list() function -> will convert other types in list type. 

t = (1,4)
print(type(t))

new_object= list(t)
print(new_object,"the type of new object is",type(new_object))

#-------------------------------------------------#
#len() function 
# len function will give us count of total elements in a list
list = [1,2,5]
print(len(list)) # 3

#------------------------------------------------#
#max function
# will find the maximum value from list
print(max(list)) # 5

#------------------------------------------------#
#min function
# will give us minimum value from the list
print(min(list)) # 1

#------------------------------------------------#

# We can concatenate the lists 
numbers = [1,2,3]
words   = ["Programming","Scripting","DevOps"]

#concatenation can be seen on the line below
new_obj = numbers + words

print(type(new_obj)) # <class 'list'>
print(new_obj) #[1, 2, 3, 'Programming', 'Scripting', 'DevOps']
