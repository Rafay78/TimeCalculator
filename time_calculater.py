def add_time(start, duration, day=None):
  n_p = ''
  start = start.split(" ")
  time = start[0]
  period = start[1]
  hours = time.split(":")[0]
  mins = time.split(":")[1]

  duration = duration.split(":")
  dur_hours = duration[0]
  dur_mins = duration[1]
  calc_hours = int(hours) + int(dur_hours)
  calc_mins = int(mins) + int(dur_mins)

  def mins_to_hrs(calc_min, calc_hours):
      if calc_min > 59:
          prep_hrs = calc_min/60
          calc_hours += int(prep_hrs)
          calc_mins = round((prep_hrs - int(prep_hrs)) * 60)
          return (calc_mins, calc_hours)

  if calc_mins > 59:
      hrs_mins = mins_to_hrs(calc_mins, calc_hours)
      calc_mins = hrs_mins[0]
      calc_hours = hrs_mins[1]

  if int(dur_hours) <= 12:
    if calc_hours > 12 and period == "PM":
        new_hour = calc_hours - 12
        n_p = "(next day)"
        new_time = f'{new_hour}:{str(calc_mins).rjust(2,"0")} AM' if not day and n_p == "" else f'{new_hour}:{str(calc_mins).rjust(2,"0")} AM {n_p}' if not day else f'{new_hour}:{str(calc_mins).rjust(2,"0")} AM, {day.title()}'
    elif calc_hours > 12 and period == "AM":
        new_hour = calc_hours - 12
        new_time = f'{new_hour}:{str(calc_mins).rjust(2,"0")} PM' if not day and n_p == "" else f'{new_hour}:{str(calc_mins).rjust(2,"0")} AM {n_p}' if not day else f'{new_hour}:{str(calc_mins).rjust(2,"0")} PM, {day.title()}'
    else:
        if int(hours) < 12 and calc_hours >= 12:
            if period == "AM":
                period = "PM"
            else:
                period = "AM"
        new_time = f'{calc_hours}:{str(calc_mins).rjust(2,"0")} {period}' if not day else f'{calc_hours}:{str(calc_mins).rjust(2,"0")} {period}, {day.title()}'

  if int(dur_hours) > 12:
      if calc_hours > 24:
          prep_days = calc_hours/24
          days = round(prep_days)

          if day:
              week = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
              for weekday in week.items():
                  if day.title() == weekday[1]:
                      counter = weekday[0]
              no_days = counter
              if (days + no_days)  <= 7:
                  day = week.get(no_days + days)
              else:
                 whole_day = (days/7)
                 prep_day = round((whole_day - int(whole_day)) * 7)
                 while prep_day:
                    if no_days + 1 > 7:
                        no_days = 0
                    no_days += 1
                    prep_day -= 1
                    day = week.get(no_days)
          hour = round((prep_days - int(prep_days)) * 24)
          if hour > 12:
              new_hour = int(hour) - 12
          else:
              new_hour = int(hour)
          n_p = f'({days} days later)' if days > 1 else "(next day)"
          if (int(hours) < 12 and hour >= 12):
            if period == "AM":
                period = "PM"
            else:
                period = "AM"
            new_time = f'{new_hour}:{str(calc_mins).rjust(2,"0")} {period} {n_p}' if not day else f'{new_hour}:{str(calc_mins).rjust(2,"0")} {period}, {day.title()} {n_p}'
          else:
            new_time = f'{new_hour}:{str(calc_mins).rjust(2,"0")} {period} {n_p}' if not day else f'{new_hour}:{str(calc_mins).rjust(2,"0")} {period}, {day.title()} {n_p}'

  return new_time
