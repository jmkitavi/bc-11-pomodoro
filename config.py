#set task time
def set_time():
    task_duration = raw_input("Enter time for task as HH:MM:SS").split(':')
    try:
        for i in [0, 1, 2]:     #check if all 3 fields are present h:m:s
            task_duration[i] = int(task_duration[i])
        return task_duration
    except:
        print "The Input wasn't Valid!"
        set_time()

#set short breaks
def short_break_settings():
    short_break = raw_input("Enter time for short break as HH:MM:SS").split(':')
    try:
        for i in [0, 1, 2]:     #check/get all 3 fields if present h:m:s
            short_break[i] = int(short_break[i])
        return short_break
    except:
        print "The Input wasn't Valid!"
        short_break_settings()

#long break settings
def long_break_settings():
    long_break = raw_input("Enter time for long break as HH:MM:SS").split(':')
    try:
        for i in [0, 1, 2]:  # check/get all 3 fields if present h:m:s
            long_break[i] = int(long_break[i])
        return long_break
    except:
        print "The Input wasn't Valid!"
        long_break_settings()

#sound seting
def sound_settings():
    sound = True
    n = raw_input("Enter 1 for Sound on or 0 for off :")
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