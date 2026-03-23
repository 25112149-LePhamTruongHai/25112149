import time

total_seconds = time.time()
seconds_in_day = 24 * 60 * 60
days_since_epoch = total_seconds // seconds_in_day

remaining_seconds = total_seconds % seconds_in_day
hours = remaining_seconds // 3600
remaining_seconds_after_hours = remaining_seconds % 3600
minutes = remaining_seconds_after_hours // 60
seconds = remaining_seconds_after_hours % 60

print(f"Days since epoch: {int(days_since_epoch)}")
print(f"Current time (GMT): {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}")
