import datetime

def display_current_datetime():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_date


def calculate_future_date(days_number):
    future_date = datetime.datetime.now() + datetime.timedelta(days=int(days_number))
    return future_date.strftime("%Y-%m-%d %H:%M:%S")


days_number = input("Enter the number of days to add to the current date: ")
print("Future date:", calculate_future_date(days_number))
