# Ask user to enter a string. 
# print all the vowels and count of vowels from the given string. 
# vowels in alphabet are a,e,i,o,u

str = input("please enter a string ")


count_of_vowels =0
index_in_str=0
vowels_in_given_str = ''
while index_in_str < len(str):
    vowels = "aeiouAEIOU"
    current_letter = str[index_in_str]
    #if the current letter is one of the chars from vowels string
    # it means we have to increase count of vowels.
    #In order to check if current letter exist in vowels str.
    if current_letter in vowels:
        count_of_vowels+=1
        vowels_in_given_str = vowels_in_given_str+current_letter

    index_in_str+=1

print(f"The all vowels in string order is {vowels_in_given_str}")
print(f"Amount of vowels we have in the given string is {count_of_vowels}")
