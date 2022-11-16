customer_name = input("Customer name : ")
total_time = int(input("Input time (minutes) : "))
hours = int(total_time//60)
remain_time = int(total_time % 60)
cost = 0
cal_hours = 0

if(remain_time != 0):
    cal_hours = 1

cal_hours += hours

if 1 <= cal_hours < 4:
    cost = 100 * cal_hours
elif 4 <= cal_hours < 7:
    cost = 90 * cal_hours
elif cal_hours >= 7:
    cost = 80 * cal_hours

if(hours >= 0):
    print("-------------------------------")
    print(f"Name : {customer_name}")
    print(f"Playtime : {hours} hr. {remain_time} min.")
    print(f"Price : {cost} baht")
    print("-------------------------------")
else:
    print("Invalid Time")
