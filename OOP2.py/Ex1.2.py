minutes = 42
seconds_remainder = 42
total_seconds = (minutes * 60) + seconds_remainder
print(f"Total seconds: {total_seconds} seconds")

kilometers = 10
km_per_mile = 1.61
total_miles = kilometers / km_per_mile
print(f"Miles in 10km: {total_miles:.2f} miles")

seconds_per_mile = total_seconds / total_miles
pace_minutes = int(seconds_per_mile // 60)
pace_seconds = int(seconds_per_mile % 60)
print(f"Average pace: {pace_minutes} minutes {pace_seconds} seconds per mile")

total_hours = total_seconds / 3600
average_speed = total_miles / total_hours
print(f"Average speed: {average_speed:.2f} mph")
