# #!/usr/bin/env python
import time
import datetime
import config
import countdown_timer


def new_task(task_name):
    x = raw_input(
        "Press [Enter] to begin the countdown with default settings or 1 to configure!\n")
    if x == "1":
        print "Configuring options for timer :"
        task_time = config.set_time()
        short_break = config.short_break_settings()
        long_break = config.long_break_settings()
        sound = config.sound_settings()
    else:
        print "Using default settings :"
        task_time = "00:00:07"
        short_break = "00:00:05"
        long_break = "00:00:06"
        sound = True

    t = time.time()
    time_stamp = str(datetime.datetime.fromtimestamp(t).strftime('%Y:%m:%d'))

    task_length = raw_input("Enter expected total task duration in HH:MM:SS :")

    def cycles(tasks_length, tasks_time):
        if countdown_timer.time_in_sec(tasks_length) < countdown_timer.time_in_sec(tasks_time):
            no_of_cycles = 1
        else:
            no_of_cycles = countdown_timer.time_in_sec(
                task_length) / countdown_timer.time_in_sec(task_time)
        return no_of_cycles

    cycles = cycles(task_length, task_time)

    x = 0
    break_status = ''
    while cycles > x:
        count = 3
        while count > 0 and cycles > x:
            x += 1
            status = countdown_timer.countdown(task_time, task_name)
            if status == 'stopped':
                break_status = 'stopped'
                break
            else:
                pass
            countdown_timer.countdown(short_break, "short break")
            count -= 1
            x += 1
        if break_status == 'stopped':
            break
        else:
            pass
        countdown_timer.countdown(task_time, task_name)
        countdown_timer.countdown(long_break, "long break")
        x += 1

new_task(" Task")
