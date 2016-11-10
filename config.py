# cycle time settings
def set_time():
    td = raw_input("Enter time for cycles as HH:MM:SS or [Enter] to use default: >")
    if td == '':
        td = "00:25:00"
        print "Using default: " + td
        return td
    else:
        task_duration = td.split(':')
        try:
            for i in [0, 1, 2]:     # check if all 3 fields are present h:m:s
                task_duration[i] = int(task_duration[i])
            return td
        except:
            print "The Input wasn't Valid!"
            set_time()
# set_time()


# long break settings
def short_break_settings():
    short_break = raw_input("Enter time for short break as HH:MM:SS or [Enter] to use default: >")
    if short_break == '':
        short_break = "00:05:00"
        print "Using default: " + short_break
        return short_break
    else:
        sb = short_break.split(':')
        try:
            for i in [0, 1, 2]:  # check if all 3 fields are present h:m:s
                sb[i] = int(sb[i])
            return short_break
        except:
            print "The Input wasn't Valid!"
            short_break_settings()


# long break settings
def long_break_settings():
    long_break = raw_input("Enter time for long break as HH:MM:SS or [Enter] to use default: >")
    if long_break == '':
        long_break = "00:15:00"
        print "Using default: " + long_break
        return long_break
    else:
        lb = long_break.split(':')
        try:
            for i in [0, 1, 2]:  # check if all 3 fields are present h:m:s
                lb[i] = int(lb[i])
            return long_break
        except:
            print "The Input wasn't Valid!"
            long_break_settings()


# sound setting
def sound_settings():
    # sound = True
    n = raw_input("Enter 1 for Sound on or 0 for off or [Enter] to use default: >")
    if n == '':
        sound = True
        print "Using default: " +str(sound)
        return sound
    else:
        if n == '0':
            sound = False
            return sound
        elif n == '1':
            sound = True
            return sound
        else:
            print "Wrong input"
            sound_settings()
        return sound


# total task length
def task_length_settings():
    task_length = raw_input("Enter total time for task as HH:MM:SS or [Enter] to use default: >")
    if task_length == '':
        task_length = "01:00:00"
        print "Using default: " + task_length
        return task_length
    else:
        tl = task_length.split(':')
        try:
            for i in [0, 1, 2]:  # check if all 3 fields are present h:m:s
                tl[i] = int(tl[i])
            return task_length
        except:
            print "The Input wasn't Valid!"
            task_length_settings()
