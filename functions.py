import datetime

def cancel():
    # print("Your appointment is cancelled")
    return "Your appointment is cancelled"
    

def show_status():
    # print("This is your appointment status")
    return "This is your appointment status"
    


def detect_relative_days(day_string):
    current_date = datetime.date.today()
    # print(current_date)

    day_name_to_weekday = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6
    }

    day_string = day_string.lower()
    # print(day_string)
    if "today" in  day_string:
        return 0

    tomorrow_date = current_date + datetime.timedelta(days=1)
    if "tomorrow" in day_string:
        return (tomorrow_date - current_date).days

    day_string_array = day_string.split()
    for i in day_string_array:
        # print(i)
        if i in day_name_to_weekday.keys():
            target_weekday = day_name_to_weekday[i]
            current_weekday = current_date.weekday()
            days_until_target = (target_weekday - current_weekday) % 7
            return days_until_target
            # if days_until_target == 0:
            #     return "It's already " + day_string.capitalize() + "!"
            # else:
            #     return f"Days until {day_string.capitalize()}: {days_until_target}"

    return None


def schedule(text):
    relative_days = detect_relative_days(text)
    print("RR",relative_days)
    if not detect_relative_days:
        # print("When do you want to schedule your appointment")
        return "When do you want to schedule your appointment"
    else:
        # print(f"Your appointment is scheduled {relative_days} day later")
        return f"Your appointment is scheduled {relative_days} day later"

# Test the function
# day_input = input("Enter a day of the week (e.g., 'Monday', 'Tuesday', 'Sunday'): ")
# relative_days = detect_relative_days(day_input)

# if relative_days is not None:
#     print(relative_days)
# else:
#     print("Invalid day input or day not recognized.")

def reschedule(text):
    relative_days = detect_relative_days(text)
    if detect_relative_days is None:
        # print("When do you want to reschedule your appointment")
        return "When do you want to reschedule your appointment"
    else:
        return f"Your appointment is scheduled {relative_days} day later"
        # print(f"Your appointment is scheduled {relative_days} day later")
        
def greet():
    # print("Hello, Weclome to MediMate. How can I help you?")
    return "Hello, Weclome to MediMate. How can I help you?"
    

def notWell():
    # print("I am sorry to hear that. Please tell me your symptoms")
    return "I am sorry to hear that. Please tell me your symptoms"