def add_time(start, duration, day=None):
    
    # Separate strings and prepare numbers for calculation
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    added_hour, added_minute = map(int, duration.split(':'))

    # Define target hour and minute printed out 
    # Convert start_hour to 24 hour clock format for easier calculating
    if period == "AM":
        if start_hour == 12:
            start_hour = 0
    elif period == "PM":
        if start_hour != 12:
            start_hour += 12
    
    # Calculate desired hour, minute, and  days for output
    total_minutes = start_minute + added_minute
    total_hours = start_hour + added_hour + (total_minutes // 60)
    minute = total_minutes % 60
    hour = total_hours % 24
    n_day = total_hours // 24
    
    # Define new periods printed out
    if hour < 12:
        final_period = "AM"
    elif hour >= 12:
        final_period = "PM"
        
    # Convert into 12 hour clock format if needed
    if hour > 12:
        hour -= 12
    elif hour == 0:
        hour = 12
    
    # Step 2 - Identify day in the week 
    # Make a list of days in a week
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Refine format of minute unit
    if minute < 10:
        time = f"{hour}:0{minute} {final_period}"
    else:
        time = f"{hour}:{minute} {final_period}"
    
    # Define final time
    if day:
        # day.index(...) is the index of current week day within the list of days in a week
        start_day_index = (days.index(day.capitalize()))
        end_day_index = (start_day_index + n_day) % 7
        end_day = days[end_day_index] # Using .capitalize() function to uppercase only the first letter of the whole word
        time += f", {end_day}"
    
    if n_day == 1:
        time += " (next day)"
    elif n_day > 1:
        time += f" ({n_day} days later)"
    
    return time
    
    
print(add_time('3:30 PM', '2:12'))                     # 1 ➜ 5:42 PM
print(add_time('11:55 AM', '3:12'))                    # 2 ➜ 3:07 PM
print(add_time('10:10 PM', '3:30'))                    # 3 ➜ 1:40 AM (next day)
print(add_time('11:59 AM', '12:01'))                   # 4 ➜ 12:00 PM  *(AM→PM boundary test)*
print(add_time('2:59 AM', '24:00'))                    # 5 ➜ 2:59 AM (next day)
print(add_time('11:59 PM', '24:05'))                   # 6 ➜ 12:04 AM (2 days later)
print(add_time('8:16 PM', '466:02'))                   # 7 ➜ 6:18 AM (20 days later)
print(add_time('3:00 PM', '0:00'))                     # 8 ➜ 3:00 PM  *(no change)*
print(add_time('3:30 PM', '2:12', 'Monday'))           # 9 ➜ 5:42 PM, Monday
print(add_time('2:59 AM', '24:00', 'saturDay'))        #10 ➜ 2:59 AM, Sunday (next day)
print(add_time('11:59 PM', '24:05', 'Wednesday'))      #11 ➜ 12:04 AM, Friday (2 days later)
print(add_time('8:16 PM', '466:02', 'tuesday'))        #12 ➜ 6:18 AM, Monday (20 days later)
