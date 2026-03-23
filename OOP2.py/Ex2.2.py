import math

radius = 5
volume = (4 / 3) * math.pi * (radius ** 3)

print(f"Thể tích hình cầu bán kính 5: {volume:.2f}")

cover_price = 24.95
discount = 0.40  
total_copies = 60

discounted_price = cover_price * (1 - discount)
shipping_cost = 3.0 + (0.75 * (total_copies - 1))
total_wholesale_cost = (discounted_price * total_copies) + shipping_cost

print(f"Tổng chi phí bán sỉ 60 cuốn sách: ${total_wholesale_cost:.2f}")

start_time_seconds = (6 * 3600) + (52 * 60)
easy_pace_seconds = (8 * 60) + 15  
tempo_pace_seconds = (7 * 60) + 12  
total_run_time = (1 * easy_pace_seconds) + (3 * tempo_pace_seconds) + (1 * easy_pace_seconds)

arrival_time_total_seconds = start_time_seconds + total_run_time
arrival_hour = arrival_time_total_seconds // 3600
arrival_minute = (arrival_time_total_seconds % 3600) // 60
arrival_second = arrival_time_total_seconds % 60

print(f"Thời gian về nhà sau khi chạy bộ: {int(arrival_hour)}:{int(arrival_minute):02d}:{int(arrival_second):02d}")
