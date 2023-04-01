#index: 0123456789.....
text = "Python is a programming language!"

part1 = text[2:6] # 
print("When we slice from index 2 to 6 the sliced part is",part1)
print("The length of sliced part is",len(part1))

part2 = text[6:3] #
print("When we slice from index 6 to 3 the sliced part is",part2)
print("The length of sliced part is",len(part2))
#In a regular slicing when starting index is bigger than ending index
# it will return an empty string. 
print("The bool value of the sliced str will be",bool(part2))

#---------------------------------------------------------------------#
#index:  0123456789.....
#text = "Python is a programming language!"
#Omitting starting or ending index
# We'll cover the output when ending or starting index 
# is not provided. 
substr = text[:4] 
print("When we slice without starting index to 4 ->",substr)
print("The length of sliced part is",len(substr))
# When starting index is not provided, slicing will start from 
# index 0.
#text[0:4] is exactly same as text[:4]
substr2 = text[1:]
print("When we slice without ending index starting from 1 ->",substr2)
print("The length of sliced part is",len(substr2))
# When the ending index for a slicing is not provided it will go 
# till the end of string. 
