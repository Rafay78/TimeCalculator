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
  if calc_hours > 12 and period == "PM":
    new_hour = calc_hours - 12
    n_p = "(next day)"

    
  calc_mins = int(mins) + int(dur_mins)
  
  new_time = f'{new_hour}:{str(calc_mins).rjust(2,"0")} {n_p}'  
  #if len(str(calc_mins)) == 1:
  	#calc_mins = str(calc_mins).insert(0,0)
  #print( new_hour,str(calc_mins).rjust(2,"0"))
  #print( dur_hours,dur_mins)
  return new_time
  
print(add_time("11:06 PM", "2:02"))
