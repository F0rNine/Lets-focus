import time

# 定义专注时间（以秒为单位）
focus_time = 45 * 60

# 定义休息时间（以秒为单位）
break_time = 5 * 60

# 循环计时器
while True:
    # 倒计时专注时间
    for i in range(focus_time, 0, -1):
        print(f"Focus time remaining: {i//60} minutes {i%60} seconds")
        time.sleep(1)

    # 专注时间结束，开始休息时间
    print("Time's up! Take a break.")
    for i in range(break_time, 0, -1):
        print(f"Break time remaining: {i//60} minutes {i%60} seconds")
        time.sleep(1)

    # 休息时间结束，开始下一轮专注时间
    print("Break time over. Let's focus!")
