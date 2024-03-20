time, step = input("").split(" ")
max_step = pow(10, 9)
step = int(step)
time = int(time) % 24
for _ in range(min(step, 1000)):  
    if time < 10:
        time = time * 2
    else:
        sum_digits = time // 10 + time % 10
        time += sum_digits
    time = int(time) % 24
    if time < 10:
        time = time * time
    else:
        sum_digits = time // 10 + time % 10
        time -= sum_digits
    time = int(time) % 24

if time == 0 or time == 9:
    print("NO")
else:
    print("YES")