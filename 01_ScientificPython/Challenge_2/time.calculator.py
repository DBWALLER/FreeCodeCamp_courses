#available at:  https://replit.com/@dbwaller/boilerplate-time-calculator#time_calculator.py

def add_time(start, duration,weekday=False):
  #Part 1:
  detailed_ini=start.replace(':', ';').replace(' ', ';')
  detailed_ini=detailed_ini.split(";")    
  #print(detailed_ini) ####

  hour_ini = int(detailed_ini[0])
  min_ini = int(detailed_ini[1])
  period_ini= detailed_ini[2]
  
  delta_time=duration.split(":")    
  #print(delta_time)

  delta_hour = int(delta_time[0])
  delta_min = int(delta_time[1])

  # Part 2 : transform initial time into integers of a 24h clock:
  # Obs.: if hour_ini = 12 PM, then it is 12h(midday/noon) in a 24h clock 
  if period_ini=="AM" and hour_ini==12: #12 AM denotes midnight
      hour_ini = 0
  if period_ini=="PM":
      if hour_ini<12:
          hour_ini=hour_ini+12  
  #else:  hour_ini = hour_ini given
  #print(hour_ini, min_ini)
  
  qt_hours= hour_ini + delta_hour  ### precisa mesmo?
  qt_min= min_ini + delta_min
  

  # Part 3A: start of calculation with hour part first
  n_24hperiod_int = delta_hour//24  
  n_days_add = qt_hours//24
  hour_add_rest= (delta_hour) - (n_24hperiod_int)*24
  hour_fin= hour_ini + hour_add_rest
  if hour_fin >=24:
      hour_fin = (hour_ini + hour_add_rest)-24


  # Part 3B:  calculation with minutes part
  qt_min= min_ini + delta_min
  if qt_min < 60:
      min_fin = qt_min
  else: #qt_min >=60:
      min_fin = qt_min-60
      #print("min_fin: ", min_fin)
  
  #correct number of hours based on the sum of minutes     
      hour_fin = hour_fin+1
      if hour_fin ==24:
        hour_fin = 0
        n_days_add=n_days_add+1
      if hour_fin>24:
        hour_fin = (hour_ini + hour_add_rest)-24+1
        n_days_add=n_days_add+1
        


  # Part 3C:  calculation of number of days added
  n_days_after = int( (qt_hours+qt_min/60)/24)


  # Part 4: reconvert to 12 h clock format
  if hour_fin==0:
      hour_fin=12
      period_fin ="AM"
  elif hour_fin==12:
      period_fin ="PM"
  elif hour_fin<=11:
      period_fin ="AM"
  else:
      hour_fin=hour_fin-12
      period_fin ="PM"


  #Part 5 - convert to string 
  hourfin = str(hour_fin)
#     if hour_fin<=9:
#         hourfin = '0'+str(hour_fin)
#     else: 
#         hourfin = str(hour_fin)
      
  if min_fin<=9:
      minfin = '0'+str(min_fin)
  else: 
      minfin = str(min_fin)
  #print(hourfin, minfin, period_fin)  



  # Part 6 :  Weekday calculation
  weekdays_list=["Monday", "Tuesday","Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
  
  if weekday is not False:
      #weekday from input
      weekday= weekday.lower().capitalize() #forst asdjut everythong to lowercase and then capitalize
      weekdays_idx_ini =  weekdays_list.index(weekday)
      #print(weekdays_idx_ini)  ###############
      sum_idx= weekdays_idx_ini + n_days_after
      if sum_idx<=6:
          idx_fin = sum_idx
      else: # >7
          n_aux = sum_idx % 7  #resto da divisao
          idx_fin = weekdays_idx_ini + n_aux -7-1
      weekday_fin = weekdays_list[idx_fin]    
      #print(weekday)
      #print(weekday_fin)  


  #Part 7 (final): adjust answers strings
  newtime = hourfin + ":" + minfin + " " + period_fin
  idx = newtime.index("M")
  if n_days_after ==1:
      newtime = newtime + " (next day)"
  if n_days_after >1:
      newtime = newtime + " (" + str(n_days_after)+" days later)"
  if weekday is not False and n_days_after >= 1:
      newtime= newtime[0:idx+1] +  ", " + weekday_fin +" "  + newtime[idx+2:]
  if weekday is not False and n_days_after <1:
      newtime= newtime[0:idx+1] +  ", " + weekday_fin
      
      
  return newtime
