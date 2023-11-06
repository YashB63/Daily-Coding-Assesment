def hands_clock(time):
    hours, minutes = map(int, time.split(':'))
    hours = hours%12
    hour_angle = (hours*30) + (minutes*0.5)
    minute_angle = minutes*6
    angle = abs(hour_angle - minute_angle)
    angle = min(angle, 360 - angle)
    return round(angle,1)
    
time = input()
result = hands_clock(time)
print(result)