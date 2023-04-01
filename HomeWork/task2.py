#String “Cookie” —> lower, replace ‘o’ with ‘u’, remove suffix e,
#starts with ‘C’

print("Cookie".lower().replace("o", "u").removesuffix("e").capitalize())





#String “ Snicker " —> strip, upper, remove prefix and slice the string with
#any number of your choice

Snicker = "  Snicker   ".strip().upper().removeprefix("S")[0:3]
print(Snicker,"14")

