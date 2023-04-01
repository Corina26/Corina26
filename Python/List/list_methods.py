#List methods
# We'll cover the commonly used list methods that alter the original value
# of lists. 
#------------------------------------------------------------------

# append method -> will add elements to the end of list.
l = [1,2]
l.append(3)
print(l) # [1,2,3]
# Since the list is mutable, the original value of the list changed
# without reassigning
#------------------------------------------------------------------

# insert method -> will add new item to the list in the given index
# insert(indexNumber, newElement)
# It will add new element WITHOUT REPLACING any existing element.
l = [1,2]
l.insert(1,"text")
print(l) # [1,"text",2]

#------------------------------------------------------------------

# remove method -> remove method removes SPECIFIED ITEM from the list.

words = ["AI","DevOps","Technology"]
#If I would like to remove one of these elements, I can just place 
# what I would like to remove in a remove method. 
#words.remove("technology")
#NOTE!!! When remove method is used with an object that is NOT IN THE LIST,
# it will GENERATE AN ERROR.
words.remove("Technology")
print(words)  #["AI","DevOps"]

#------------------------------------------------------------------
#pop method -> will remove element from specified INDEX
words = ["AI","DevOps","Technology"]
words.pop(1)
print(words) # ["AI","Technology"]

#words.pop(4)
#NOTE!!! When pop method used with index that doesn't exist in a list,
# it WILL GENERATE AN ERROR
