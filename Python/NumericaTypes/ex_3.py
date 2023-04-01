# A DevOps engineer needs to monitor the remaining time for a 
# long-running task on a server. They have the total time the task
#  takes in hours, minutes, and seconds, and they know the time that
#   has already passed. They want to calculate the remaining time for
#    the task to complete.

# Step 1: Define the problem inputs.

# Total time for the task (hours, minutes, seconds)
# Time passed (hours, minutes, seconds)
total_hours = 5
total_minutes = 25
total_seconds = 15

passed_hours = 2
passed_minutes = 45
passed_seconds = 30


def remaining_time(total_hours, total_minutes, total_seconds, passed_hours, passed_minutes, passed_seconds):
    # Convert the total time and passed time into seconds.
    print("yo=",total_hours * 3600)
    total_time_seconds = (total_hours * 3600) + (total_minutes * 60) + total_seconds
    passed_time_seconds = (passed_hours * 3600) + (passed_minutes * 60) + passed_seconds

    # Calculate the remaining time in seconds.
    remaining_time_seconds = total_time_seconds - passed_time_seconds

    # Convert the remaining time in seconds back to hours, minutes, and seconds.
    remaining_hours = remaining_time_seconds // 3600
    remaining_minutes = (remaining_time_seconds % 3600) // 60
    remaining_seconds = remaining_time_seconds % 60

    # Return the remaining time as a tuple (hours, minutes, seconds)
    return remaining_hours, remaining_minutes, remaining_seconds


# Example usage:
total_hours = 5
total_minutes = 25
total_seconds = 15

passed_hours = 2
passed_minutes = 45
passed_seconds = 30

remaining_hours, remaining_minutes, remaining_seconds = remaining_time(total_hours, total_minutes, total_seconds, passed_hours, passed_minutes, passed_seconds)
print("Remaining time: {} hours, {} minutes, {} seconds".format(remaining_hours, remaining_minutes, remaining_seconds))


remaining_hours, remaining_minutes, remaining_seconds = remaining_time(5, 30, 30, 6, 15, 1)
print("Remaining time: {} hours, {} minutes, {} seconds".format(remaining_hours, remaining_minutes, remaining_seconds))


