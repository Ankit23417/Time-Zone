import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print (hour)
Min = int(time.strftime('%M'))
print (Min)
Sec = int(time.strftime('%S'))
print (Sec)
# hour= int(input("enter hour"))
# print(hour)
if (hour>=4 and hour<12):
    print("Good  morning Ankit")
elif (hour>=12 and hour<17):
    print("Good afternoon Ankit")
elif (hour>=17 and hour<20):
    print("Good  evening Ankit")
else:
    print("Good  night Ankit")