from datetime import datetime
def display_current_datetime():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_date

daysNumber = input("Enter the number of days to add to the current date: ")

def calculate_future_date():
    future_date = datetime("%Y-%m-%d %H:%M:%S", daysNumber)
    print(future_date)
    # future_date = display_current_datetime() + future_date
    return future_date

print("Future date:",calculate_future_date())