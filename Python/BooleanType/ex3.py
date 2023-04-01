# Veera wants lose 10 pounds in one month. 
# There are multiple conditions to lose 10 pounds in a month 
# Veera needs to walk 10000 steps daily  OR needs to run at least
#  4 miles a day.  and Addition to these , Veera needs eat less 
#  than 1500 calories daily. 
#  We should create a program to calculate if Veera can 
#  loose weight or not.

# define the necessary variables and values
target_weight_loss = 10  # pounds
target_monthly_calorie_deficit = 1500 * 30  # assuming a 30-day month
target_daily_steps = 10000
target_daily_miles = 4

# get input from user
daily_steps = int(input("Enter the number of steps you take daily: "))
daily_miles = float(input("Enter the number of miles you run daily: "))
 
daily_calories = int(input("Enter the number of calories you consume daily: "))
nume = str(input("Numele: "))

# calculate the total monthly calorie deficit
daily_calorie_deficit = daily_calories - 1500
monthly_calorie_deficit = daily_calorie_deficit * 30

# check if Veera can achieve the target weight loss
if (daily_steps >= target_daily_steps or daily_miles >= target_daily_miles) and monthly_calorie_deficit >= target_monthly_calorie_deficit:
    print(nume,"Congratulations, you can lose 10 pounds in one month!")
else:
    print(nume,"Sorry, it may not be possible to lose 10 pounds in one month with your current daily routine and calorie intake.")

