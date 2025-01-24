import pandas as pd
from datetime import datetime, timedelta


def generate_single_hour_window(date, past_len=6, future_len=6, interval=3):

    past_hours = [date - timedelta(hours=interval * i) for i in range(past_len)][::-1]

    future_hours = [date + timedelta(hours=interval * (i+1)) for i in range(future_len)]

    return past_hours, future_hours


def generate_hour_windows(start_date, end_date, past_len=6, future_len=6, interval=3):

    total_window_list = []

    current_date = start_date

    while current_date <= end_date:

        x, y = generate_single_hour_window(current_date, past_len, future_len, interval)
        total_window_list.append((x, y))

        current_date += timedelta(hours=1)

    return total_window_list



if __name__ == "__main__":

    # x, y = generate_single_hour_window(date=datetime(2021, 3, 14, 0), past_len=6, future_len=6, interval=3)

    total_window_list = generate_hour_windows(
        start_date=datetime(2021, 3, 14, 0),
        end_date=datetime(2021, 3, 15, 23),
        past_len=6,
        future_len=6,
        interval=3
    )


    print("debug")