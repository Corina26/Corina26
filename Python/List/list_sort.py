# Create a program that sorts list 
# without using sort method. 

list = [0,2,5,11,100,6,200,1]

# max() -> will give me maximum number

sorted_list = []

while len(list) != 0:
    max_num = max(list)
    sorted_list.insert(0,max_num)
    list.remove(max_num)

print(sorted_list)
