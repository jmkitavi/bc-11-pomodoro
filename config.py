# cycle time settings
def set_time():
    td = raw_input("Enter time for cycles as HH:MM:SS : >")
    task_duration = td.split(':')
    try:
        for i in [0, 1, 2]:     # check if all 3 fields are present h:m:s
            task_duration[i] = int(task_duration[i])
        return td
    except:
        print "The Input wasn't Valid!"
        set_time()


# long break settings
def short_break_settings():
    short_break = raw_input("Enter time for short break as HH:MM:SS : >")
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
    long_break = raw_input("Enter time for long break as HH:MM:SS : >")
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
    sound = True
    n = raw_input("Enter 1 for Sound on or 0 for off : >")
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
    task_length = raw_input("Enter total time for task as HH:MM:SS : >")
    tl = task_length.split(':')
    try:
        for i in [0, 1, 2]:  # check if all 3 fields are present h:m:s
            tl[i] = int(tl[i])
        return task_length
    except:
        print "The Input wasn't Valid!"
        task_length_settings()
