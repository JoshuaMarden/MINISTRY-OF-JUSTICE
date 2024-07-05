"""test 3"""
from datetime import datetime


# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.


def get_system_time() -> str:
    """Returns the current system time as a string."""
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def sum_current_time(time_str: str = get_system_time()) -> int:
    """Sum time string in format HH:MM:SS"""
    list_of_nums = time_str.split(":")
    return sum(int(number) for number in list_of_nums)

if __name__ == "__main__":
    print(sum_current_time())
