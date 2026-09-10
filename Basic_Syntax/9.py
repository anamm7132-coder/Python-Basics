import time 
timestamp=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
if (hour>4 and hour<13):
    print("GOOD MORNING SIR")
elif(hour>12 and hour <18):
    print("GOOD AFTERNOON SIR")
elif(hour>17 and hour<24):
    print("GOOD EVENING SIR")
