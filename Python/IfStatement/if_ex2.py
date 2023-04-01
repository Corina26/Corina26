#  getting ticket for speed violation
#   in state of IN, speed limit on HighWays is 70  
#   in other states, speed limit on Highways is 55
#   -if driver exceeds speed limit for up to 10% of the limit in each state, 
#    we will give WARNING in that state
#     state of IN warning means --> print --> "YELLOW WARNING"
#     other state warnings mean --> print --> "CITATION"
# -if driver exceeds speed limit more than 10% of the limit in each state,
#  we will give TICKET in that state
#     state of IN ticket means --> print --> "$150 and 5 points"
#     other state ticket means --> print --> "$100"
# -if speed is same as  speed limit or lower, --> print --> "You are driving safe!"
# Note SL -> Speed Limit

# State they are in
# Compare driver's speed with more than speed limit. 
# If they are going lower than SL print going safe
# If they are faster than SL we should check if they are going up to 10 percent or more
# If it is more than even up to 10 percent we should print ticket otherwise give warning.

driver_speed = int(input("Enter your speed -> "))
state_code = input("Enter your state code: -> ").upper()
if state_code == "IN":
    speed_limit = 70

    if driver_speed <= speed_limit:
        print( "You are driving safe!")
        # On the line below we have to find how much the driver exceed speed limit.
        # If driver exceeds more than 10 percent of the SL, driver should get a ticket.
    elif   driver_speed > (speed_limit+speed_limit*0.1):
        print("$150 and 5 points")  
    else:
        print("YELLOW WARNING")
else:
    speed_limit = 55

    if driver_speed <= speed_limit:
        print( "You are driving safe!")
        # On the line below we have to find how much the driver exceed speed limit.
        # If driver exceeds more than 10 percent of the SL, driver should get a ticket.
    elif   driver_speed > (speed_limit+speed_limit*0.1):
        print("$100")  
    else:
        print( "CITATION")







