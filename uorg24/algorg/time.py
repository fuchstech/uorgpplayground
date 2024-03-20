inp = input("")
time,step = inp.split(" ")
max_step = pow(10,9)
if not 0<=int(time)<=24:
    print("Invalid time")
    exit()
if not 0<int(step)<=max_step:
    print("Invalid step")
    exit()
    
step = int(step)
for i in range(0,step):
    if len(time) == 1:
        time  = str(int(time)*2) # if time is single digit sum it with itself
    else:
        time = str(int(time)+int(time[0]) + int(time[1])) # if time is double digit sum it with its digits
        
    if len(time) == 1:
        time  = str(int(time)*int(time)) # if time is single digit minus it with itself
    else:
        time = str(int(time)-(int(time[0]) + int(time[1]))) # if time is double digit minus it with its digits
if time == "0" or time == "9":
    print("No")
else: 
    print("Yes")
