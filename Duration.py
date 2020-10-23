
def format_duration(seconds):
    if seconds == 0:
        return 'now'
    year,day,hour,minute = 365*(3600*24),3600*24,3600,60
    years,days,hours,minutes,second = 0,0,0,0,0
    while seconds != 0:
        if seconds >= year:
            years = seconds // year
            seconds = seconds - years*year

        elif seconds < year and seconds >= day:
            days = seconds // day
            seconds = seconds - days*day

        elif seconds < day and seconds >= hour:
            hours = seconds // hour
            seconds = seconds - hours*hour

        elif seconds < hour and seconds >= minute:
            minutes = seconds // minute
            seconds = seconds - minute*minutes

        elif seconds < minute:
            second = seconds
            seconds = 0

    time  = {'years':years, 'days':days, 'hours':hours, 'minutes':minutes, 'seconds':second}
    time_0 = {}
    for key in time:
        if time[key] != 0:
            if time[key] == 1:
                time_0[key[:-1]] = time[key]
            else:
                time_0[key] = time[key]

    if len(time_0) == 1:
        for key in time_0:
            return str(time_0[key]) + ' ' + key
    elif len(time_0) == 2:
        time_list = []
        for key in time_0:
            time_list.append((key, time_0[key]))
        return str(time_list[0][1]) + " " + time_list[0][0] + " and " + str(time_list[1][1]) + " " + time_list[1][0]
    elif len(time_0) > 2:
        time_list = []
        for key in time_0:
            time_list.append((key, time_0[key]))
        count = 0
        while count < len(time_0)-1:
            if count == 0:
                output = str(time_list[0][1]) + " " + time_list[0][0]
            else:
                output += ", " + str(time_list[count][1]) + " " + time_list[count][0]
            count += 1
        return output + " and " + str(time_list[-1][1]) + " " + time_list[-1][0]

print(format_duration(3666))