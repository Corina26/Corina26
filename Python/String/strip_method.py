# Using a strip method without providing a parameter will give us
# the new string value after removing spaces at the end and beginning of 
# string

str = "We like programming         "

print(len(str)) # The length is 28

after_strip_method = str.strip()

print("the length of string after the strip method is",len(after_strip_method))

# Using strip method with the parameter
# It removes the given parameter from the end and beginning of the 
# string. 
phone_num = "###8888#88888#####"
# To be able to get the number itself we have to get rid of the 
# number signs. 

without_sign = phone_num.strip("#")
print(without_sign) #8888#88888
