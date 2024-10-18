import time

def get_alarm_time():
    while True:
        alarm_time = input("Enter the time for the alarm in 24-hour format (e.g., 07:30): ")
        # Validate time format
        if validate_time_format(alarm_time):
            return alarm_time
        else:
            print("Invalid time format. Please enter again.")

def validate_time_format(time_str):
    """Validate the input time format (HH:MM)."""
    try:
        time.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False

def wait_for_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}. Waiting...")
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Alarm is going off!")
            break
        time.sleep(30)  # Check every 30 seconds to avoid busy waiting

def main():
    alarm_time = get_alarm_time()
    wait_for_alarm(alarm_time)

if __name__ == "__main__":
    main()
