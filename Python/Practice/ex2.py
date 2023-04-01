# create a function to find highest common factor of two given numbers.
# highest common factor is a biggest common divisor of two given numbers.
# 24 18 -> 6 -> There is no number bigger than 6 that could evenly divide 24 and 18.
# 32 12 -> 4
# 24 12 -> 12 

#  What is the limit of the numbers  I should check as a possible HCF ? 
#  I have two numbers given, my limit as possible HCF should be one of the numbers and below.
#  I should chose one of the numbers start checking from that number to number 1. 
#  When writing a code, first do necessities of the code. Then optimize
#
def find_HCF(num1,num2):
    possible_hcf = num1
    while True:
        if num1 % possible_hcf == 0 and num2 % possible_hcf == 0:
            # It is not a possibility that possible hcf can divide both, 
            # it is a certainty. 
            return possible_hcf
          
        # I should tell the code look next possible option
        possible_hcf -= 1

print(find_HCF(24,32))
print(find_HCF(32,24))

print(find_HCF(32,12))