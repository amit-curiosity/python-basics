from datetime import datetime

current_time = datetime.now()

print(f"current_date: {current_time.date().strftime('%d/%m/%Y')}")
print(f"current_time: {current_time.time().strftime('%H:%M:%S')}")
