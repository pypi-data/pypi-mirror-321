import datetime as dt

from datetime import datetime, timedelta




def convert_datetime_to_str(time):

    year = str(time.year).zfill(4)
    month = str(time.month).zfill(2)
    day = str(time.day).zfill(2)
    hour = str(time.hour).zfill(2)
    minute = str(time.minute).zfill(2)

    return year, month, day, hour, minute

def convert_list_to_datetime(date_list):
    # 根据列表长度决定如何处理
    if len(date_list) == 3:  # 年月日
        year, month, day = date_list
        return datetime(year=year, month=month, day=day)
    elif len(date_list) == 4:  # 年月日时
        year, month, day, hour = date_list
        return datetime(year=year, month=month, day=day, hour=hour)
    elif len(date_list) == 5:  # 年月日时分
        year, month, day, hour, minute = date_list
        return datetime(year=year, month=month, day=day, hour=hour, minute=minute)
    else:
        raise ValueError("输入的列表长度不支持，请提供长度为 3（年月日）、4（年月日时）或 5（年月日时分）的列表")
