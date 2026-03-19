minutes = 42
seconds = 42
km = 10

total_seconds = minutes*60 + seconds
miles = km / 1.61

print('seconds:', total_seconds)
print('miles:', miles)

pace_minutes = (minutes + seconds/60) / miles
pace_seconds = (minutes*60 + seconds) / miles
print('pace:', pace_minutes, 'min/mile')

speed = miles / (minutes/60 + seconds/3600)
print('speed:', speed, 'mph')
