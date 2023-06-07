import datetime

# 把字符串转成Datetime格式
def tranformStrToDateTime(timeStr='') -> datetime.datetime:
    try:
        if '.' in timeStr:
            timeStr = timeStr.split(".")[0]
        else:
            timeStr = timeStr[:-1]
        timeArray = datetime.datetime.strptime(timeStr, "%Y-%m-%dT%H:%M:%S")
    except:
        print(timeStr)
    return timeArray

# 检查给定时间是否晚于限制时间
def checkTimeIsMoreThan(time=datetime.datetime, timeLimit=()) -> bool:
    # 时间上限
    yearUp = timeLimit[2]
    monthUp = timeLimit[3]

    year = time.year
    month = time.month
    if year > yearUp:
        return True
    elif year == yearUp:
        if month > monthUp:
            return True
        else:
            return False
    else:
        return False

# 检查时间是否早于限制时间
def checkTimeIsLessThan(time=datetime.datetime, timeLimit=()) -> bool:
    year = time.year
    month = time.month

    # 时间下限
    yearDown = timeLimit[0]
    monthDown = timeLimit[1]

    if year < yearDown:
        return True
    elif year == yearDown:
        if month < monthDown:
            return True
        else:
            return False
    else:
        return False

# 判断传入的时间是否符合时间限制
def checkTime(time=datetime.datetime, timeLimit=()) -> bool:
    if not isinstance(time, datetime.datetime):  # 新增类型判断 2020.12.30
        return False
    if checkTimeIsMoreThan(time, timeLimit):
        return False
    elif checkTimeIsLessThan(time, timeLimit):
        return False
    else:
        return True

# 把字符串转成Datetime格式
def tranformStrToDateTime(timeStr='') -> datetime.datetime:
    try:
        if '.' in timeStr:
            timeStr = timeStr.split(".")[0]
        else:
            timeStr = timeStr[:-1]
        timeArray = datetime.datetime.strptime(timeStr, "%Y-%m-%dT%H:%M:%S")
    except:
        print(timeStr)
    return timeArray