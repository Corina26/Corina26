# From the two given lists find all common elements

l  = ["n","1",1,2,3]
l2 = ["n",3,"1",10,11,"new","n","1",3]



# We could solve this question in two ways:
set_v1 = set(l)
set_v2 = set(l2)

common_set = set_v1.intersection(set_v2)
print(common_set)

# Other way



l  = ["n","1",1,2,3]
l2 = ["n",3,"1",10,11,"new","n","1",3]


common_set = set()

for element in l2:
    # element definetely is in l2 
    if element in l:
        common_set.add(element)

print(common_set)
