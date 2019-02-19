def ConvertSectoDay(n): 
    months = n //(24 * 3600 * 30)
    n = n % (24 * 3600 * 30)
    
    day = n // (24 * 3600) 
  
    n = n % (24 * 3600) 
    hour = n // 3600
  
    n %= 3600
    minutes = n // 60
  
    n %= 60
    seconds = n 
      
    print(months, "months", day,"days", hour, "hours",  
          minutes, "minutes", 
          seconds, "seconds")
    

total_distance = 10000
speed = int(input("speed: "))
n = total_distance / speed
n = n *60 * 60
ConvertSectoDay(n)

    
